# String Utils with Unit Tests

## 项目目的

这是一个简单的字符串工具库，提供三个常用函数：

- `reverse_words(s)`：反转字符串中单词的顺序
- `count_vowels(s)`：统计字符串中英文元音字母（a, e, i, o, u）的数量，忽略大小写
- `is_palindrome(s)`：判断字符串是否为回文，忽略大小写和空格

本项目同时演示了如何使用 `pytest` 给 Python 函数编写单元测试，覆盖正常情况、边界情况以及异常情况。

## 安装 pytest

使用 pip 安装 pytest：

```bash
pip install pytest
```

如果你的系统同时存在 Python 2 和 Python 3，请使用：

```bash
pip3 install pytest
```

## 运行测试

在项目目录下运行：

```bash
pytest -v
```

`-v` 参数会显示每个测试用例的详细名称和通过情况。
