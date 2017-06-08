#liuxue_outputer
class LiuxueOutputer(object):

    def open():
        f = open('outputen.txt','w',errors='ignore')
        f.write("学校key值\t")
        f.write("所在省份\t")
        f.write("学校名称\t")
        f.write("所在城市\t")
        f.write("专业数\t")
        f.write("中国学生数\t")
        f.write("在校留学生数\t")
        f.write("院校官网\t")
        f.write("留学生受理部门网址\t")
        f.write("院校介绍\t")
        f.write("国际课程记录数量\t")
        for i in range(20):
            f.write("国际课程记录"+str(i+1)+"\t")
            f.write("国际课程记录"+str(i+1)+"详细记录\t")
        f.write("住宿信息数量\t")
        for i in range(8):    
            f.write("房间类型"+str(i+1)+"\t")
            f.write("住宿费"+str(i+1)+"\t")
            f.write("卫生间"+str(i+1)+"\t")
            f.write("浴室"+str(i+1)+"\t")
            f.write("宽带"+str(i+1)+"\t")
            f.write("固定电话"+str(i+1)+"\t")
            f.write("空调"+str(i+1)+"\t")
            f.write("其他"+str(i+1)+"\t")
        f.write("住宿展示图片数\t")
        f.write("联系人\t")
        f.write("联系电话\t")
        f.write("Email\t")
        f.write("联系网址\t")
        f.write("邮编\t")
        f.write("地址\n")
        f.flush()
        return f

    def collect(f,data):
        f.write(data['key']+'\t')
        f.write(data['shengfen']+'\t')
        f.write(data['school_name']+'\t')
        f.write(data['city']+'\t')
        f.write(data['pro_num']+'\t')
        f.write(data['china_num'] +'\t')
        f.write(data['fore_num'] +'\t')
        f.write(data['net']+'\t')
        try:
            f.write(data['fore_net']+'\t')
        except:
            f.write("无记录\t")
        f.write(data['about']+'\t')
        f.write(data['record_count']+'\t')
        for i in range(20):
            f.write(data['record'+str(i+1)]+"\t")
            f.write(data['record'+str(i+1)+'detail']+'\t')
        f.write(str(data['zhusu_count'])+'\t')
        for i in range(8):    
            f.write(data['fjlx'+str(i+1)]+"\t")
            f.write(data['zsf'+str(i+1)]+"\t")
            f.write(data['wsj'+str(i+1)]+"\t")
            f.write(data['ys'+str(i+1)]+"\t")
            f.write(data['kd'+str(i+1)]+"\t")
            f.write(data['gddh'+str(i+1)]+"\t")
            f.write(data['kt'+str(i+1)]+"\t")
            f.write(data['qt'+str(i+1)]+"\t")
        f.write(str(data['pic_count'])+'\t')
        f.write(data['man']+'\t')
        f.write(data['phone']+'\t')
        f.write(data['email']+'\t')
        f.write(data['lianxiwangzhi']+'\t')
        f.write(data['youbian']+'\t')
        f.write(data['lianxiadress']+'\n')
        f.flush()

    def close(f):
        f.close()
