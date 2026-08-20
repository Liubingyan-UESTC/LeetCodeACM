# test_code.py 使用说明

`test_code.py` 是一个本地 ACM 风格算法题验证脚本：只需指定题解文件名，就会自动读取当前目录下 `io/input.txt` 作为标准输入，并调用题解中的 `main()`。

## 基本用法

在任意工作目录下执行：

```bash
python test_code.py <file_name>
```

示例：

```bash
python test_code.py combination_sum
# 或带后缀
python test_code.py combination_sum.py
```

等价流程：

1. 在 `~/std/LeetCode/` 根目录或某个算法分类子目录（`hashmap/`、`dp/` 等）中查找题解
2. 从**当前工作目录**的 `io/input.txt` 读取输入
3. 将 `stdin` 重定向为该输入文件
4. 导入题解模块并调用 `main()`

## 目录约定

| 路径 | 作用 |
|------|------|
| `~/std/LeetCode/<分类目录>/<file_name>.py` | 算法实现文件（按分类放在二级目录，如 `hashmap/combination_sum.py`） |
| `~/std/LeetCode/<file_name>.py` | 兼容：根目录下仍可直接放置/加载题解 |
| `~/std/LeetCode/templates/` | 公共模板（链表/二叉树等），不属于题解，不会被检索 |
| `./io/input.txt`（当前工作目录下） | ACM 格式输入数据 |
| `./io/output.txt`（可选） | 期望输出，可自行对照 |

因此：

- 题解文件按算法类型放在 `~/std/LeetCode/` 的二级分类目录下（如 `hashmap/`、`dp/`、`doubleptr/`、`slidingwindow/`、`linkedlist/`、`binarytree/`、`graph/`、`mathmatic/`）
- 只需文件名即可定位，脚本会自动在根目录及各分类目录中检索；也可直接传目录路径，如 `python test_code.py hashmap/combination_sum`
- 测试时在含有 `io/` 目录的工作目录下运行脚本
- 同一题换测试数据时，只需改 `io/input.txt`，不用改题解

## 题解文件约定

实现文件只需提供算法逻辑和入口 `main()`，不必手写读文件或测试驱动代码。

推荐写法：

```python
import sys

input = sys.stdin.readline


def solve():
    # 用 input() 按 ACM 方式读入，用 print 输出
    n = int(input())
    ...
    print(answer)


def main():
    solve()
```

要求：

1. 必须定义可调用的 `main()`
2. 通过标准输入读数据（`sys.stdin` / `input()`）
3. 通过标准输出打印结果（`print`）

说明：

- `if __name__ == "__main__": main()` 可以写，也可以不写；被 `test_code.py` 导入时不会自动执行该分支
- 若模块顶层有 `input = sys.stdin.readline`，脚本会在导入前完成 stdin 重定向，保证读取的是 `io/input.txt`

## 输入文件示例

`io/input.txt`（ACM 模式，按行给出）：

```text
4
2 7 11 15
9
```

对应题解 `combination_sum.py` 中用 `input()` 逐行读取即可。

## 完整示例

假设：

- 题解：`~/std/LeetCode/hashmap/combination_sum.py`（含 `main()`）
- 当前目录有 `io/input.txt`

执行：

```bash
cd ~/std/LeetCode
python test_code.py combination_sum
```

终端会打印算法对 `io/input.txt` 的运行结果。

## 常见错误

| 报错 | 原因 | 处理 |
|------|------|------|
| `Usage: python test_code.py <file_name>` | 未传文件名或参数过多 | 只传一个题解名 |
| `solution not found: ...` | 根目录及所有分类子目录下都没有对应 `.py` | 检查文件名、所属分类目录 |
| `ambiguous solution name ...` | 同名题解同时存在于多个目录 | 用目录路径明确指定，如 `hashmap/combination_sum` |
| `input file not found: .../io/input.txt` | 当前目录缺少 `io/input.txt` | 先写好输入，或 `cd` 到含有 `io/` 的目录 |
| `... must define callable main()` | 题解缺少 `main()` | 补充入口函数 |

## 设计目的

写新题时只需：

1. 新建 `~/std/LeetCode/<分类目录>/<题名>.py`，实现算法与 `main()`
2. 准备 `io/input.txt`
3. 运行 `python test_code.py <题名>`

无需在每个题解里重复编写「读文件 / 构造测试 / 调用入口」的样板代码。
