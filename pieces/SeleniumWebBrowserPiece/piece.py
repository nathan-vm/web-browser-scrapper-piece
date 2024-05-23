from domino.base_piece import BasePiece
from .models import InputModel, OutputModel, CommandOutput
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumWebBrowserPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        self.logger.info("Create chrome options arguments.")

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")

        self.logger.info("Start chrome web driver.")
        driver = webdriver.Chrome(options=options)

        self.logger.info("Going to URL.")
        driver.get("https://webscraper.io/test-sites/e-commerce/static")

        self.logger.info("Maximize window.")
        driver.maximize_window()

        self.logger.info("Taking screenshot.")
        driver.save_screenshot('ss.png')

        self.logger.info("Quit chrome driver.")
        driver.quit()

        return OutputModel(
            outputs=[dict(name="out1", result="res1")]
        )
