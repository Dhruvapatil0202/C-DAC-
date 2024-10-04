package Day07.Classwork.NewEmployeeApp;

public class Department {
    private String empid;
    private String deptname;

    public Department(int empid, String deptname) {
        this.empid = empid;
        this.deptname = deptname;
    }

    @Override
    public String toString() {
        return "Department{" +
                "empid='" + empid + '\'' +
                ", deptname='" + deptname + '\'' +
                '}';
    }

    public String getEmpid() {
        return empid;
    }

    public void setEmpid(String empid) {
        this.empid = empid;
    }

    public String getDeptname() {
        return deptname;
    }

    public void setDeptname(String deptname) {
        this.deptname = deptname;
    }
}
