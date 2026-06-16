import express from 'express';
import multer from 'multer';
import path from 'path';
import fs from 'fs';
import cors from 'cors';

const app_node = express();
const port = 3000;

// 使用 cors 中间件
app_node.use(cors());

// 设置 Multer 存储
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    const dir = '../public/pic/AD';
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    cb(null, dir);
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

app_node.use(express.json());
app_node.use(express.urlencoded({ extended: true }));

app_node.post('/posts', upload.array('images'), (req, res) => {
  const { username, title, price, address, description } = req.body;
  const files = req.files;

  const imageUrls = files.map(file => `/pic/AD/${files.filename}`);

  console.log(files[0])

  res.json({
    message: '图片上传成功！',
    imageUrls: imageUrls,
    image: files[0].filename
  });
});

app_node.use('/pic/AD', express.static(path.join(process.cwd(), 'pic/AD')));

app_node.listen(port, () => {
  console.log(`服务器运行在 http://localhost:${port}`);
});
