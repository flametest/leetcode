为某家医院设计一套（专家）挂号系统。

 

专家医生排班后即确定了每天的出诊时间，排班的最小时间段为半天（上午/下午），每个时间段的号源有限，挂满为止。

 

就诊流程为：

 

选择就诊科室

根据选择的科室，给出给定天数内，每一天的上午及下午分别有哪些医生出诊以及每位医生的剩余号源数量

就诊人选择某位医生有剩余号源的时段，进入支付流程

支付成功后，挂号成功

 

Q. 请以符合第三范式为原则，设计出该系统在关系数据库中需要的表以及关键的字段，并描述表之间的关系。

 

附：2022年1~5月

 

全国门诊人次约 1,600,000,000 (16亿人次)，平均每月超过 3亿人次

北京门诊人次约 55,000,000 (5千5百万人次)， 平均每月 1千万人次


Doctor
    id: int
    name: string
    max_capacity: int
    department_id: int

Department:
    id: int
    name: string

//每个科室每半天一个schedule
Schedule:
    id: int
    department_id: int
    start_at: timestamp
    end_at: timestamp
    max_capacity: int // 科室的capacity

//同一个科室多个doctor排班, 对应每个doctor的capacity
//如何判断doctor时间被占用？
DoctorSchedule:
    id: int
    doctor_id: int
    schedule_id: int 
    capacity: int

    unique_index(doctor_id, schedule_id)


Ticket:
    id: int
    department_id: int
    doctor_schedule_id: int
    patient_id: int

Patient:
    id: int
    name: string

Payment:
    id: int
    ticket_id: int
    state: enum // created, pending, success

select s.department_id, ds.doctor_id, max(capacity)  from doctor_schedule ds join schedule s on ds.schedule_id = s.id 
where s.start_at between DAY_START and DAY_END
group by s.department_id









