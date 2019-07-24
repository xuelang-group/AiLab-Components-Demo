# coding=utf-8
from __future__ import absolute_import, print_function

import os

from sklearn.externals import joblib

import suanpan
from suanpan.model import Model
from suanpan.stream import Handler as h
from suanpan.stream import Stream
from suanpan.stream.arguments import Float, Json, String


class ModelDemo(Model):
    def load(self, path):
        self.model = joblib.load(os.path.join(path, "model.model"))

    def predict(self, features):
        return self.model.predict(features)


class ModelStreamDemo(Stream):
    ARGUMENTS = [
        String(key="model1", required=True),  # 设置model路径参数，--model1为第一个model的路径
        Float(key="param1", alias="duration", default=10),  # 设置加载模型duration参数
    ]

    def afterInit(self):  # 初始化模型
        self.model = ModelDemo()
        self.model.setLoader(storagePath=self.args.model1, version="latest")
        self.model.load(self.model.path)

    def afterCall(self):  # 在每一次call()之后，检查是否有新的模型版本， 有的话会自动下载相应版本模型文件夹
        self.model.reload(self.args.duration)

    @h.input(Json(key="inputData1", required=True))
    @h.output(Json(key="outputData1"))
    def call(self, context):

        args = context.args

        inputData = args.inputData1
        print("input data: {}".format(inputData))

        features = None  # 获取数据

        outputData = self.model.predict(features)  # 预测
        print("output data: {}".format(outputData))

        return outputData  # 返回结果


if __name__ == "__main__":
    suanpan.run(ModelStreamDemo)
