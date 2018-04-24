###Screen
删除会话：  

	 screen -X -S 会话id quit
	 
     还可以直接 kill 该会话的id，在执行screen -wipe 清除无用的会话。

创建会话：  

	screen -S 会话名称

从会话切出来：
	
	Alt+A+D

分离会话：
	
	screen -d 会话名称

查看会话列表：

	screen -ls

进入某会话：

	screen -r 会话名称

