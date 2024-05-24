from domino.base_piece import BasePiece
from .models import InputModel, OutputModel,CommandInput, CommandOutput
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
class SeleniumWebBrowserPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        self.logger.info("Create chrome options arguments.")

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")

        self.logger.info("Start chrome web driver.")
        driver = webdriver.Chrome(options=options)

        results_path = Path(self.results_path)

        for cmd in input_data.commands:
            if cmd.name.value == "save_screenshot":
                cmd.value = str(results_path/cmd.value)
                self.display_result = dict(file_type="png",filepath=cmd.value)
            
            if cmd.name.value is None:
                getattr(driver, cmd.name)()
            else:
                getattr(driver, cmd.name)(cmd.value)    
        
        driver.quit()

        return OutputModel(
            outputs=[dict(name="out1", result="res1")]
        )
 