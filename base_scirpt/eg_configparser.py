import configparser

filename = "/tmp/my.cnf"
cfg = configparser.ConfigParser()
cfg.read(filename)
print(len(cfg))
sections = cfg.sections()
for sect in sections:
    print(sect,type(sect))
    options = cfg.options(sect)
    print(options,type(options))
    for option in options:
        val = cfg.get(sect,option)
        print(sect,'/ ',option,'=',val,type(val))

port = cfg.getint('mysqld','port')
print(port,type(port))

print('~~~~~~~~~~~~~~~~~~~')
print(cfg.items())

for k,_ in cfg.items():
    print(k,cfg.items(k))
    
print('~~~~~~~~~~~~~~~~~~~')

print(cfg)
print(cfg._sections.keys())
print(cfg.sections())
print(cfg['mysqld']['port'])

#如果section已经存在就会报错，必须是不存在
cfg.add_section('testsec3')
cfg['testsec3']['b'] = str([1,3,5])
with open(filename,'w') as f:
    cfg.write(f)

cfg.add_section('sunnytest01')
cfg.add_section('sunnytest03')
with open(filename,'w') as f:
    cfg.write(f)
