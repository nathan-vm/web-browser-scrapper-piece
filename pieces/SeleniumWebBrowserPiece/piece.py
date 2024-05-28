from domino.base_piece import BasePiece
from .models import InputModel, OutputModel,CommandInput, CommandOutput
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
from typing import List
import json
class SeleniumWebBrowserPiece(BasePiece):

    def piece_function(self, input_data: InputModel):
        self.logger.info("Create chrome options arguments.")

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")

        self.logger.info("Start chrome web driver.")
        self.driver = webdriver.Chrome(options=options)

        outputs = self.run_commands(commands=input_data.commands)

        self.driver.quit()

        return OutputModel(
            outputs=outputs
        )

    def run_commands(self, commands: List[CommandInput]) -> List[str]:
        results_path = Path(self.results_path)

        outputs: List[str] = []

        for idx, cmd in enumerate(commands):
            result = ""

            self.logger.info(f"commands[{idx}] - {cmd.name}" + (f": {cmd.value}" if cmd.value else ""))

            if cmd.name.value == "get":
                self.driver.get(cmd.value)

            if cmd.name.value == "current_url": 
                result = self.driver.current_url

            if cmd.name.value == "save_screenshot":
                cmd.value = str(results_path/cmd.value)
                self.driver.save_screenshot(cmd.value)
                result = cmd.value

            if cmd.name.value == "find_element_css":
                result = self.driver.find_element(By.CSS_SELECTOR, cmd.value).text

            if cmd.name.value == "find_elements_css":
                elements = self.driver.find_elements(By.CSS_SELECTOR, cmd.value)
                result = []
                for e in elements:
                    result.append(e.get_attribute('innerHTML'))

            if not isinstance(result,str):
                result = str(result)

            outputs.append(result)

        return outputs