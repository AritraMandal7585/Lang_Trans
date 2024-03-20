# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:12:45 2024

@author: aritr
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add OPTIONS method
    allow_headers=["*"],
)

class ModelInput(BaseModel):
    lang: str
    
@app.post('/translation')
async def translation(input_parameters: ModelInput):
    try:
        model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
        tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
        model_inputs = tokenizer(input_parameters.lang, return_tensors="pt")
        generated_tokens1 = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
        generated_tokens2 = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["bn_IN"])
        translation1 = tokenizer.batch_decode(generated_tokens1, skip_special_tokens=True)
        translation2 = tokenizer.batch_decode(generated_tokens2, skip_special_tokens=True)
        return {"Hindi": translation1, "Bangla": translation2}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
