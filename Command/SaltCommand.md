### 命令行删除文件
#### linux
    cmdtest:
      cmd.run:
        #- onlyif: /data/crawler/spider/code/che_zhu_jia_ge/extroactor.py
        - names:
          #- rm -rf /data/crawler/spider/code/jiang_jia/setting.py
          #- export redis_id='1230999'
        #- user: root
#### win
    因为配置文件方式的没有找到对应的win的命令，所有win的就用命令行，linux也是可以的。
    salt 'web_*' file.remove E:\\one.pyc

<hr>
### 复制文件：
     最后一个是minion上文件地址
    "salt 'web*' cp.get_file salt://code_file/one.pyc E://one.pyc"


