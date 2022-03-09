FROM biansepang/weebproject:buster

RUN git clone -b main https://github.com/msy1717/Beast-X1.2/root/beastx
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/beastx

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/msy1717/Beast-X1.2/main/requirements.txt

CMD ["python3",""beast-x1.2.py"]
