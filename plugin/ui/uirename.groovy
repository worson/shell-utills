import java.io.File;

public class IconRenamer {



    public static void main(String[] args) {
        renameDirIcons("/Users/wangshengxing/Downloads/rent_app/test","Group 8.png","icon.png");
    }

    public static void renameDirIcons(String path, String sName, String dName) {
        File dir = new File(path);
        if (!dir.exists()) {
            print("文件不存在");
        }
        File[] files=dir.listFiles(new FileFilter() {
            @Override
            public boolean accept(File pathname) {
                return pathname.getName().contains("drawable");
            }
        });
        if (files != null) {
            for (File file : files) {
                File srcFile=new File(file.getName()+"/"+sName);
                if (srcFile.exists()) {
                    boolean success= false;
                    try {
                        success = srcFile.renameTo(new File(file.getName()+"/"+dName));
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    print(srcFile.getAbsolutePath()+",success="+success);
                }

            }
        }
    }

    private static void print(String msg) {
        System.out.println(msg);
    }

}


IconRenamer renamer = new IconRenamer();
renamer.main(null);

