from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from typing import List
import uuid
import pickle

class GetHTMLPiece(BasePiece):

    def piece_function(self, input_data: InputModel) -> OutputModel:
        results_path = Path(self.results_path)
        outputs: List[str] = []

        self.logger.info("Create chrome options arguments.")

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")

        self.logger.info("Start chrome web driver.")
        driver = webdriver.Chrome(options=options)

        for url in input_data.get_page_html:
            driver.get(url)
            page_html = driver.page_source
            outputs.append(page_html)

        driver.quit()

        file_name = f"{results_path}/{uuid.uuid4()}.pkl"

        with open(file_name,"wb") as file:
            pickle.dump(outputs, file)
        
        return OutputModel(
            output_file_path=file_name
        )