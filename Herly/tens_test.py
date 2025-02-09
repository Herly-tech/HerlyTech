#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""An Example of a DNNClassifier for the Iris dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf

import iris_data  # 本地电脑没有测试数据和训练数据时


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')

def main(argv):
    args = parser.parse_args(argv[1:])

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = iris_data.load_data()  #获取数据

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(   # DNNClassifier深度神经网络分类器  estimator调用一个或多个方法，传递适当的输入函数作为数据的来源
        feature_columns=my_feature_columns, #
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],  #两个隐藏层，每个层10个节点
        # The model must choose between 3 classes.
        n_classes=3)  # 结果为3类 参考官方网站

    # Train the Model.
    classifier.train(  #训练模型的函数
        input_fn=lambda:iris_data.train_input_fn(train_x, train_y,
                                                 args.batch_size), #检查可用率
        steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:iris_data.eval_input_fn(test_x, test_y,
                                                args.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],  #传递三个鸢尾花的特征，得到数据相应的分类
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }

    predictions = classifier.predict(
        input_fn=lambda:iris_data.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=args.batch_size))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(iris_data.SPECIES[class_id],
                              100 * probability, expec))


if __name__ == '__main__':  #当前函数在运行的时候，执行下面代码。 如果当成模块导入时不会执行
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)



"""
出现了版本不兼容，
通过命令行查看：conda search package_name --info

比如查看seaborn的信息，在命令行输入conda search seaborn --info，可以查看seaborn各版本的信息（包括依赖包的信息）：统一模块版本

"""