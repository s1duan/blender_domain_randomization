# blender_domain_randomization

This repository uses dockerized Blender (version 2.92) as well as randomization scripts to generate dataset that can be used in deep learning model training.
1. Build docker image from the dockerfile
```
docker build -t blender .
```
2. Run docker image in background
```
docker run -dit blender
```

