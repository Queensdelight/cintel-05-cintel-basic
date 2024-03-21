# --------------------------------------------
# Imports at the top
# --------------------------------------------

from shiny import App, render, ui, reactive
import random
from datetime import datetime

# --------------------------------------------
# Define the Shiny UI layout
# --------------------------------------------

app_ui = ui.page_fluid(
  ui.card(
    "Antarctic Temperature",
    ui.output_text_verbatim("output_display_temp", placeholder=True),
    ui.output_text_verbatim("output_display_time", placeholder=True),
  )
)

# --------------------------------------------
# Reactive calc with temp and timestamp
# Function to generate a random temperature between -20 and 35 and current timestamp
# --------------------------------------------

@reactive.calc()
def reactive_calc_generate_data():
  # Schedule this reactive expression to invalidate every second
  reactive.invalidate_later(1)  #  every 1 second

  temp = round(random.uniform(-20, 35), 2)
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  return {"temp": temp, "timestamp": timestamp}

# --------------------------------------------
# Shiny Core 
# Define the server logic to render the UI components based on reactive values
# ---------------------------------------------

def server(input, output, session):
  @output
  @render.text
  def output_display_temp():
    data_dictionary = reactive_calc_generate_data()
    return f"{data_dictionary['temp']}°C"

  @output
  @render.text
  def output_display_time():
    data_dictionary = reactive_calc_generate_data()
    return f"{data_dictionary['timestamp']}"

# --------------------------------------------
# Create and run the app
# --------------------------------------------
app = App(app_ui, server)
