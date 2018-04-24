### 命令行删除文件

#### win
    salt 'web_*' file.remove E:\\one.pyc

#### linux
    cmdtest:
      cmd.run:
        #- onlyif: /data/crawler/spider/code/che_zhu_jia_ge/extroactor.py
        - names:
          #- rm -rf /data/crawler/spider/code/jiang_jia/jiang_jia.py
          #- rm -rf /data/crawler/spider/code/jiang_jia/setting.py
          #- export redis_id='1230999'
        #- user: root


#### 复制文件：
     最后一个是minion上文件地址
    "salt 'web*' cp.get_file salt://code_file/jiang_jia.py E://app_code//jiangjia//jiang_jia.py",
    "salt 'web*' cp.get_file salt://code_file/setting.py E://app_code//jiangjia//setting.py",
    "salt 'web*' cp.get_file salt://code_file/one.pyc E://one.pyc"


