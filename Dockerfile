FROM python:3.7
LABEL maintainer hialireahotonnagnon@gmail.com

WORKDIR /api
COPY . /api
ENV TZ='Asia/Shanghai'
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ENTRYPOINT ["python","run.py"]