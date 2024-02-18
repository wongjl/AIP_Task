#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: wjinglun
"""

from transformers import pipeline


class Model():
    def __init__(self):
        self.nlp = pipeline(
            "document-question-answering",
            model="impira/layoutlm-document-qa",
        )

    def predict_answer(self, image_url, question_txt):
        output = self.nlp(image_url, question_txt)[0]

        return output