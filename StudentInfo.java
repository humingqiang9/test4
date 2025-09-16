public class StudentInfo {
    // 学生属性
    private String name;
    private int id;
    private int age;
    private String major;
    private double gpa;

    // 构造方法
    public StudentInfo() {
        this.name = "";
        this.id = 0;
        this.age = 0;
        this.major = "";
        this.gpa = 0.0;
    }

    public StudentInfo(String name, int id, int age, String major, double gpa) {
        this.name = name;
        this.id = id;
        this.age = age;
        this.major = major;
        this.gpa = gpa;
    }

    // 访问器方法 (Getters)
    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public int getAge() {
        return age;
    }

    public String getMajor() {
        return major;
    }

    public double getGpa() {
        return gpa;
    }

    // 修改器方法 (Setters)
    public void setName(String name) {
        this.name = name;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public void setGpa(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) {
            this.gpa = gpa;
        } else {
            System.out.println("错误：GPA必须在0.0到4.0之间");
        }
    }

    // 其他方法
    public void displayInfo() {
        System.out.println("学生信息:");
        System.out.println("姓名: " + name);
        System.out.println("学号: " + id);
        System.out.println("年龄: " + age);
        System.out.println("专业: " + major);
        System.out.println("GPA: " + gpa);
    }

    public String getGradeLevel() {
        if (age <= 18) {
            return "大一";
        } else if (age <= 19) {
            return "大二";
        } else if (age <= 20) {
            return "大三";
        } else {
            return "大四或以上";
        }
    }

    public boolean isHonorStudent() {
        return gpa >= 3.5;
    }

    // toString方法
    @Override
    public String toString() {
        return "StudentInfo{" +
                "name='" + name + '\'' +
                ", id=" + id +
                ", age=" + age +
                ", major='" + major + '\'' +
                ", gpa=" + gpa +
                '}';
    }
}