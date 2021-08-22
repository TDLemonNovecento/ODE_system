#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(deSolve)
library(tidyverse)
library(ggpmisc)


## Parameters
VV <- 2.17     # Vitreous volume (mL) 2.0–2.5 :L/min).
VR <- 0.073   # Retia volume (mL)
VA <- 0.13   # Aqueous volume (mL)

# additional unknown variables
# Sources:
# awwad2015 Proteins have longer half-lives (i.e., days to weeks)
# in the vitreous than RCS26 permeable molecules (e.g., lipophilic
#  molecules 500 Da), which generally are a matter of
# hours.

V1 <- 0.5
V2 <- 5

ClA <- 0.3
Cl <- 0.5
kR <- 0.2
kVR <- 1.5
kVA <- 1.2

Q <- V1+V2
f <- 0.5



# Define server logic required to draw a histogram
shinyServer(function(input, output) {

    #Here comes the plotting
    
    output$Plot <- renderPlot({
        
        # generate timesteps based on input$timesteps and
        # input$days from ui.R
        times <- seq(from=0,to=input$days,by=input$timestep/(12*60))
        
        #input starting dose as specified
        xstart <- c(V=0,A=0, R=0, S=0, P=0)
        xstart[input$startcomp][1] <- input$startdose
        
        # get all parameters that can be adjusted as well as those fixed
        # into a column
        ## Parameters
        VV <- 2.17     # Vitreous volume (mL) 
        VR <- 0.073   # Retia volume (mL)
        VA <- 0.13   # Aqueous volume (mL)
        
        parms <- c(VV=VV, VA=VA, VR=VR,
                   V1=input$V1,
                   V2=input$V2,
                   ClA=input$ClA,
                   Cl=input$Cl,
                   kR=input$kR,
                   kVR=input$kVR,
                   kVA=input$kVA,
                   Q=input$Q,
                   f=input$f)
        
        # Create PK model function
        eye.PK.model <- function (t, x, params) {
            ## first extract the state variables
            V <- x[1] #ng substance in systemic compartment
            A <- x[2] #ng substance in peripheral compartment
            R <- x[3] #ng substance in R compartment
            S <- x[4] #ng substance in systemic compartment
            P <- x[5] #ng substance in peripheral compartment
            
            
            ## now extract the parameters
            VV <- params["VV"] #volume V compartment
            VA <- params["VA"] #volume A compartment
            VR <- params["VR"] #volume R compartment
            V1 <- params["V1"] #volume systemic compartment
            V2 <- params["V2"] #volume peripheral compartment
            ClA <- params["ClA"] #clearance from A compartment
            Cl <- params["Cl"] #clearance from system
            kR <- params["kR"] #rate from R compartment to systemic compartment
            kVR <- params["kVR"]
            kVA <- params["kVA"]
            Q <- params["Q"]
            f <- params["f"] #fraction??
            
            kRV <- kVR*VV/VR
            
            k12 <- Q/V1
            k21 <- Q/V2
            
            
            ## now code the model equations
            dRdt <- -R*kR- R*kRV + V*kVR
            dVdt <- -V*kVR + R*kRV - V*kVA
            dAdt <- V*kVA - A*ClA/VA
            dSdt <- -Cl*S/V1+ 2*f*A*ClA/VA + 2*f*R*kR + k21*P - k12*S
            dPdt <- -k21*P + k12*S
            
            ## combine results into a single vector
            dxdt <- c(dVdt,dAdt,dRdt, dSdt, dPdt)
            ## return result as a list!
            list(dxdt)
        }
        
        #solve system of ODE
        ode(
            func=eye.PK.model,
            y=xstart,
            times=times,
            parms=parms
        ) %>%
            as.data.frame() -> out


        ##convert results (mg) to concentrations (ug/ml)
        cout <- data.frame(time = out['time'])
        cout['dVcdt'] <- out['V']/VV *  1000
        cout['dAcdt'] <- out['A']/VA *  1000
        cout['dRcdt'] <- out['R']/VR *  1000
        cout['dScdt'] <- out['S']/V1  *  1000
        cout['dPcdt'] <- out['P']/V2 * 1000
        
        #get maximal values of concentrations
        maxconc <- data.frame(x = seq(1,5), comp = c("A", "V", "R", "S", "P"))
        maxconc["time"] <- c(out$time[which(out$A == max(out$A))],
                                                 out$time[which(out$V == max(out$V))],
                                                 out$time[which(out$R == max(out$R))],
                                                 out$time[which(out$S == max(out$S))],
                                                 out$time[which(out$P == max(out$P))])
        maxconc["max. conc."] <-c(max(out$A), max(out$V),max(out$R),max(out$S),max(out$P) )
        
        gridExtra::grid.arrange(
            out %>%
                gather(variable,value,-time) %>%
                ggplot(aes(x=time,y=value,color=variable))+
                geom_line(size=2)+
                theme_classic()+
                labs(title="Drug in compartment [mg]",
                     x='time (days)',y='concentration'),
            cout %>%
                gather(variable,value,-time) %>%
                ggplot(aes(x=time,y=value,color=variable))+
                geom_line(size=2)+
                theme_classic()+
                labs(title="Concentration of drug in compartment [mg]",
                     x='time (days)',y='concentration') +
                annotate(geom = "table",
                         x = +Inf, y = +Inf, label = list(maxconc %>% 
                                                        mutate_if(is.numeric, round, digits = 2))),
            nrow = 2
            )

    })
})

