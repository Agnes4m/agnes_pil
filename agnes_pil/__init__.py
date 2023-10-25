# 画图
from pydantic import BaseModel, Field
from PIL import Image, ImageDraw

from config import font
import asyncio


class Simple(BaseModel):
    text: str
    title: str = Field("标题")
    size: int = Field(20)
    width: int = Field(400)
    line: int = Field(30)
    padding: int = Field(20)

    async def make(self):
        """测算长宽"""
        # 文本内容
        text = self.text
        # 图像宽度
        image_width = self.width
        # 文本区域距离边界的距离
        padding = self.padding
        # 每行字符数
        chars_per_line = self.line

        # 加载字体

        # 按每行字符数拆分文本
        lines = [
            text[i : i + chars_per_line] for i in range(0, len(text), chars_per_line)
        ]

        # 计算文本区域的高度
        line_height = font.getsize("A")[1]  # 使用字体中任意字符的高度作为参考
        text_area_height = line_height * len(lines)

        # 计算图像的高度
        image_height = 2 * padding + text_area_height

        # 创建图像
        image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        # 计算文本绘制的起始位置
        start_x = padding
        start_y = padding

        # 逐行绘制文本
        for line in lines:
            # 计算当前行文本的大小
            line_width, line_height = draw.textsize(line, font=font)
            # 计算当前行文本的绘制位置
            line_x = start_x + (image_width - 2 * padding - line_width) // 2
            line_y = start_y
            # 绘制文本
            draw.text((line_x, line_y), line, font=font, fill=(0, 0, 0))
            # 更新下一行的起始位置
            start_y += line_height

        # 保存图像
        image.save("output.png")


if __name__ == "__main__":
    a = Simple(
        text="你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a你好a "
    )
    asyncio.run(a.make())
