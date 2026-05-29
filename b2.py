# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee[0]

# Lấy họ tên nhân viên
full_name = employee["name"]

# Cập nhật trạng thái nhân viên
employee["employee_status"] = "official"

# Thêm lương cơ bản
employee.append("base_salary", 15000000)

# Xóa phòng ban
del employee["team"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)

# Phân tích lỗi :

# Hãy trả lời các câu hỏi sau:

# Dictionary employee gồm những key nào?
# Vì sao dòng sau gây lỗi?
# employee_id = employee[0]
# Dictionary có truy cập phần tử bằng index giống list không?
# Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?

# # Dictionary gồm các keys employeee_vid , full_name ,department,status 
# Dòng gây lỗi keyerrorr là dotrong dict không có key là 0 nên khi gọi 0 sẽ bị báo lỗi ,
# Dect không ruy cập phần tử bằng index như list , nó sẽ truy cập bằng các gọi value theo key tương ứng của phần tử 
# Muốn lấy mã nhân viên NV001 ta cần viét lại : employee_id = employee.get('employee_id')

# vì sao dòng sau gây lỗi?
# full_name = employee["name"]
# Key đúng để lấy họ tên nhân viên là gì?

# Lệnh sau gây lỗi keyerror là do key name không có ở trong dict employee dẫn tới khi chạy chương trình báo lỗi.
# Key đúng của họ tên nhân viên là full_name 

# Vì sao dòng sau chưa cập nhật đúng trạng thái nhân viên?
# employee["employee_status"] = "official"
# Muốn cập nhật trạng thái nhân viên, cần dùng key nào?

# Dòng sau không cập nhật đúng trạng thái nhân viên là do cập nhật sai status , tên key bị sai khiến báo lỗi keyeror va không cập nhật được .
# muốn cập nhật đúng trạng thái nhân viên cần cập nhật lại key -> status đúng với như key ở trong dict 

# Vì sao dòng sau gây lỗi?
# employee.append("base_salary", 15000000)
# Dictionary có phương thức append() không?
# Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?
# Đoạn code này gây lỗi vì thực hiện cú pháp thêm phần tử sai , trong dict không có phượng thức append() để thực hiện thêm ,
# muốn thêm lương cơ bản cần viết như sau : employee['base_salary'] = 15000000

# Vì sao dòng sau gây lỗi?
# del employee["team"]
# Muốn xóa thông tin phòng ban, cần dùng key nào?

# vì trong dict không chứa key nào tên là team nên sẽ gây lỗi.
# muốn xóa thông tin phòng ban cần dùng key department .

# code 
# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee['employee_id']

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee['base_salary'] = 15000000

# Xóa phòng ban
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)