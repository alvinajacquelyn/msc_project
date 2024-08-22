import os
import zipfile
import sys

def apk2dext(filepath,dexdir):

    apkfile = zipfile.ZipFile(filepath,'r')
    apkname = str(apkfile.filename).split('\\')[-1][:-4]
    print(apkname)
 
    if os.path.isdir('dex') == False:
        os.mkdir('dex')
    for tempfile in apkfile.namelist(): 
        if tempfile.endswith('.dex'):
            dexfilename = apkname + '.dex'   
            f = open(dexdir + '\\'+ dexfilename,'wb+')
            f.write(apkfile.read(tempfile))


def main():
    dexdir = 'android_dex'
    apkdir = 'jar2dexandroid_apk'
    # apkdir = sys.argv[1]
    # dexdir = sys.argv[2]

    for file_name in os.listdir(apkdir):
        if file_name.endswith(".apk"):
            apk_file_path = os.path.join(apkdir, file_name)
            # print(apk_file_path)
            try:
                apk2dext(apk_file_path,dexdir)
                print(f"Successfully processed: {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue



main()