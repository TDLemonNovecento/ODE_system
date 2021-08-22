#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

    # Application title
    titlePanel("System of ODE behaviour"),

    # Sidebar with a slider input for number of bins
    sidebarLayout(
        sidebarPanel(
            radioButtons("startcomp",
                         "In which compartment should a dose of drug be administered at start?",
                         choices = list("Aqueous Chamber" = "A", 
                                        "Vitrious Chamber" = "V", 
                                        "Retina" = "R",
                                        "Systemic" = "S",
                                        "Peripheral" = "P"),
                         selected = "V"),
            
            numericInput("startdose",
                         "What dose should be administered at start? [mg]",
                         value = 10),
            
            sliderInput("days",
                        "Number of days:",
                        min = 1,
                        max = 60,
                        value = 20),
            numericInput("timestep",
                "Minutes between simulation steps:",
                min = 0,
                max = 60,
                value = 2),
            
            # input all the values for ODE system
            numericInput("V1",
                         "Volume of systemic compartment:",
                         value = 130),
            numericInput("V2",
                         "Volume of peripheral compartment:",
                         value = 245),

            numericInput("ClA",
                         "Clearance from Aqueous:",
                         min = NA,
                         max = NA,
                         step = 0.1,
                         value = 0.3),
            numericInput("Cl",
                         "Clearance from Systemic compartment: [/day]",
                         min = NA,
                         max = NA,
                         step = 0.1,
                         value = 22),
            numericInput("kR",
                         "Elimination from Retinal compartment:",
                         min = NA,
                         max = NA,
                         step = 0.1,
                         value = 0.2),
            numericInput("kVR",
                         "Vitreous-to-retina partition coefficient:",
                         min = NA,
                         max = NA,
                         value = 7.3),
            numericInput("kVA",
                         "Vitreous-to-aqueous partition coefficient",
                         value = 4.4),
            numericInput("Q",
                         "Intercompartment clearance between\n systemic and peripheral compartment:",
                         value = 440),
            
            numericInput("f",
                         "bioavailability of mediator to transport drug into systemic compartment",
                         value = 0.8),
        ),
        

        # Show a plot of the generated distribution
        mainPanel(
            plotOutput(outputId = "Plot", height = 800)
        )
    )
))

