from domino.base_piece import BasePiece
from .models import InputModel, OutputModel, CommandOutput
from selenium import webdriver

class SeleniumWebBrowser(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Execution started")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)

        driver.get("https://webscraper.io/test-sites/e-commerce/static")

        self.logger.info("Maximizing window")
        driver.maximize_window()

        driver.quit()

        return OutputModel(
            outputs=[CommandOutput(name="out1", result="res1")]
        )
