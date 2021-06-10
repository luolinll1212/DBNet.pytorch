# -*- coding: utf-8 -*-
import os


def check_file(path):
    if os.path.exists(path):
        os.remove(path)
    fp = open(path, "w", encoding="utf-8")
    fp.close()


def gen_label(dataset, mode, label):
    # 列出图片
    image_path = os.path.join(dataset, mode, "image")
    gt_path = os.path.join(dataset, mode, "gt")

    # 检查标签
    check_file(label)

    with open(label, "w", encoding="utf-8") as fwrite:
        # 提取图片
        for file in os.listdir(image_path):
            # 获取图片路径
            full_img_path = os.path.join(image_path, file)
            print(full_img_path)

            # 获取标签
            label = file.split(".")[0]
            gt = f"gt_{label}.txt"

            # 获取标签路径
            full_gt_path = os.path.join(gt_path, gt)

            line = "{} {}\n".format(full_img_path, full_gt_path)

            # 写入数据
            fwrite.write(line)


def main():
    # 生成训练集标签文件
    dataset = "data/idcar2015"
    mode = "train"
    label = os.path.join(dataset, "train.txt")
    gen_label(dataset, mode, label)

    # 生成测试集标签文件
    dataset = "data/idcar2015"
    mode = "test"
    label = os.path.join(dataset, "test.txt")
    gen_label(dataset, mode, label)


if __name__ == '__main__':
    main()

