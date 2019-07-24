# coding=utf-8
from __future__ import absolute_import, print_function

import suanpan
from suanpan.spark import SparkComponent as sc
from suanpan.spark.arguments import ListOfString, Table


@sc.input(Table(key="inputData", table="inputTable", partition="inputPartition"))
@sc.column(ListOfString(key="columns"))
@sc.output(Table(key="outputData", table="outputTable", partition="outputPartition"))
def Demo(context):
    args = context.args

    df = args.inputData

    if args.columns:
        df = df.select(args.columns)

    return df


if __name__ == "__main__":
    suanpan.run(Demo)
