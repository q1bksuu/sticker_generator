# api

## heart_name_heart

### /heart_name_heart/generate

#### method GET

生成“爱心-名字-爱心”的表情

#### 模板

![heart_empty.jpg](static/image/heart_empty.jpg)

#### 参数说明

| 字段名      | 意义         | 类型      | 是否必传 | 默认值   | 注释         |
|:---------|:-----------|:--------|------|-------|:-----------|
| name     | 白板上的文字     | string  | 是    |       | 字符串长度1~8   |
| angle    | 白板上文字的旋转角度 | number  | 否    | 5     | 范围-180~180 |
| download | 是否下载成文件    | boolean | 否    | false |            |

#### 例
1. /heart_name_heart/generate?name=你好

![heart_empty.jpg](example/heart_name_heart/heart_hello_heart.jpg)
