#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/16
# @File Name: main.py

import os
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.post('/static/{theme}/{filename}')
@app.get('/static/{theme}/{filename}')
async def static(theme: str, filename: str):
    return FileResponse(f'static/{theme}/{filename}')
