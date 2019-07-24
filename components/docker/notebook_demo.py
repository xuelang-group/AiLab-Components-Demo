# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.docker import DockerComponent
from suanpan.docker.arguments import Folder
from suanpan.notebook import Notebook

notebook = Notebook(DockerComponent, "Demo")
# 定义输入
notebook.input(Folder(key="inputData1", required=True))
# 定义输出
notebook.output(Folder(key="outputData1", required=True))

context = notebook.init()
args = context.args

print(args.inputData1)
# 自定义代码
utils.hello()

# 将 args.outputData1 作为输出发送给下一节点
notebook.save(context, arsgs.outputData1)
