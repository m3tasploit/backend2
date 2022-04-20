import base64

from flask import Flask,render_template,request,session,jsonify
from DBConnection import Db
app = Flask(__name__)
app.secret_key='abc'

@app.route('/home')
def home():
    return render_template("admin/homepage.html")





@app.route('/adm_add_dept')
def adm_add_dept():
    return render_template("admin/department_add.html")

@app.route('/adm_add_dept_post',methods=["post"])
def adm_add_dept_post():
    dname=request.form['deptname']
    qry="insert into department(depname) values ('"+dname+"')"
    db=Db()
    db.insert(qry)
    return "<script>alert('Department name Added'); window.location='/adm_add_dept'</script>";

@app.route('/adm_view_dept')
def adm_view_dept():
    db=Db()
    qry=db.select("select * from department")

    return render_template("admin/department_view.html",data=qry)

@app.route('/adm_edit_dept/<id>')
def adm_edit_dept(id):
    db=Db()
    qry=db.selectOne("select * from department where depid='"+id+"' ")

    return render_template("admin/department_edit.html",data=qry)

@app.route("/adm_update_dept_post",methods=["post"])
def adm_update_dept_post():
    db=Db()
    did=request.form['idd']
    dname=request.form['deptname']
    qry=db.update("update department set depname='"+dname+"' where depid='"+did+"'")
    return adm_view_dept()

@app.route('/adm_delete_dept/<id>')
def adm_delete_dept(id):
    db=Db()
    qry=db.delete("delete from department where depid='"+id+"'")

    return adm_view_dept()









@app.route('/adm_add_course')
def adm_add_course():
    db=Db()
    qry=db.select("select * from department")
    return render_template("admin/course_add.html",data=qry)


@app.route('/adm_add_course_post',methods=['post'])
def adm_add_course_post():
    cname=request.form['cname']
    cyear=request.form['cyear']
    dep=request.form['select']
    qry="insert into course(coursename,depid,cyear) values ('"+cname+"','"+dep+"','"+cyear+"')"
    db=Db()
    db.insert(qry)
    return "<script>alert('coursename and corseyear Added'); window.loaction='/adm_add_course'; </script>"

@app.route('/adm_view_course')
def adm_view_course():
    db=Db()
    qry=db.select("select course.*,department.depname from course,department where course.depid=department.depid")
    return render_template("admin/course_view.html",data=qry)

@app.route('/adm_edit_course/<id>')
def adm_edit_course(id):
    db=Db()
    qry=db.selectOne("select department.depname,course.* from department,course where course.depid=department.depid and course.courseid='"+id+"'")
    qry1=db.select("select * from department")
    return render_template("admin/course_edit.html",data=qry,data2=qry1)

@app.route('/adm_update_course',methods=["post"])
def adm_update_course():
    db=Db()
    coursename=request.form['cname']
    courseid=request.form['courseid']
    courseyear=request.form['cyear']
    dep=request.form['select']
    qry=db.update("update course set coursename='"+coursename+"',depid='"+dep+"',cyear='"+courseyear+"' where courseid='"+courseid+"'")
    return adm_view_course()

@app.route('/adm_delete_course/<id>')
def adm_delete_course(id):
    db=Db()
    qry=db.delete("delete from course where courseid='"+id+"'")
    return adm_view_course()










@app.route('/adm_add_student')
def adm_add_student():
    db=Db()
    qry=db.select("select * from course")

    return render_template("admin/student_add.html",data=qry)

@app.route('/adm_add_student_post',methods=["post"])
def adm_add_student_post():
    db=Db()
    name=request.form['sname']
    admno=request.form['adnum']
    coursename=request.form['select']
    semester=request.form['sem']
    gender=request.form['gender']
    guardian=request.form['guaname']
    dob=request.form['dob']
    phoneno=request.form['phoneno']
    mail = request.form['email']
    # image=request.form['fileupload']

    files=request.files["fileupload"]
    files.save("C:\\backend\\static\\imgs\\"+files.filename)

    image= "/static/imgs/"+files.filename



    qry=db.insert("insert into student(stuname,admno,courseid,semester,gender,guardian,dob,phoneno,email,image) values('"+name+"','"+admno+"','"+coursename+"','"+semester+"','"+gender+"','"+guardian+"','"+dob+"','"+phoneno+"','"+mail+"','"+image+"')")
    return "<script>alert('information added');window.location='/adm_add_student';</script>"

@app.route('/adm_view_student')
def adm_view_student():
    db=Db()
    qry=db.select("select student.*,course.coursename from course,student where course.courseid=student.courseid")
    return render_template("admin/student_view.html",data=qry)

@app.route('/adm_edit_student/<idd>')
def adm_edit_student(idd):
    db=Db()
    qry=db.selectOne("select course.courseid as cid,course.coursename,student. * from student,course where student.courseid=course.courseid and student.stuid='"+idd+"'")
    qry1=db.select("select * from course")
    session['kk']=idd
    return render_template("admin/student_edit.html",data=qry,data1=qry1)

@app.route('/adm_update_student_post',methods=['post'])
def adm_update_student_post():
    db=Db()
    # print("kkkkkkkk")
    x=session['kk']
    # print(x)
    stuname=request.form['sname']
    admno=request.form['adnum']
    courseid=request.form['select']
    semester=request.form['sem']
    gender=request.form['gender']
    guardian=request.form['guaname']
    dob=request.form['dob']
    phoneno=request.form['phoneno']
    email=request.form['email']
    qry=db.update("update student set stuname='"+stuname+"',admno='"+admno+"',courseid='"+courseid+"',semester='"+semester+"',gender='"+gender+"',guardian='"+guardian+"',dob='"+dob+"',phoneno='"+phoneno+"',email='"+email+"' where stuid='"+str(x)+"'")
    return adm_view_student()

@app.route('/adm_delete_student/<id>')
def adm_delete_student(id):
    db=Db()
    qry=db.delete("delete from student where stuid='"+id+"'")
    return adm_view_student()




@app.route('/adm_add_notification')
def adm_add_notification():
    return render_template("admin/notification_add.html")

@app.route('/adm_add_notification_post',methods=['post'])
def adm_add_notification_post():
    notcon=request.form['notcon']
    notdat=request.form['notidate']
    notexp=request.form['expdate']
    qry="INSERT INTO notification(notcontent,notdate,expirydate)values ('"+notcon+"','"+notdat+"','"+notexp+"')"
    db=Db()
    db.insert(qry)
    return "<script>alert('notcontent,notdate,expdate Added');window.location='/adm_add_notification';</script>"

@app.route('/adm_view_notification')
def adm_view_notification():
    db=Db()
    qry=db.select("select * from notification")
    return render_template("admin/notification_view.html",data=qry)

@app.route('/adm_edit_notfn/<m>')
def adm_edit_notfn(m):
    db=Db()
    # print("hloooooooo")
    qry="select * from notification where notid='"+m+"'"
    res=db.selectOne(qry)
    session['m']=m
    return render_template("admin/notification_edit.html",data=res)

@app.route('/adm_update_notification_post',methods=['post'])
def adm_update_notification_post():
    db=Db()
    x=session['m']
    notcon=request.form['notcont']
    notdate=request.form['notidate']
    expdate=request.form['expdate']
    qry=db.update("update notification set notcontent='"+notcon+"',notdate='"+notdate+"',expirydate='"+expdate+"' where notid='"+str(x)+"'")
    return adm_view_notification()


@app.route('/adm_delete_notification/<id>')
def adm_delete_notification(id):
    db=Db()
    qry=db.delete("delete from notification where notid='"+id+"'")
    return adm_view_notification()





@app.route('/adm_add_election')
def adm_add_election():
    return render_template("admin/election_add.html")

@app.route('/adm_add_election_post',methods=['post'])
def adm_add_election_post():
    elname=request.form['elname']
    eledate=request.form['datetime']
    status=request.form['status']
    qry="INSERT into election(elename,dateandtime,status)values ('"+elname+"','"+eledate+"','"+status+"')"
    db=Db()
    db.insert(qry)
    return "<script>alert('elename,eledateandtime,status added');window.location='/adm_add_election'</script>"


@app.route('/adm_view_election')
def adm_view_election():
    db=Db()
    qry=db.select("select * from election")
    return render_template("admin/election_view.html",data=qry)

@app.route('/adm_edit_election/<id>')
def adm_edit_election(id):
    db=Db()
    qry=db.selectOne("select * from election where eleid='"+id+"'")
    return render_template("admin/election_edit.html",data=qry)

@app.route('/adm_update_election_post',methods=['post'])
def adm_update_election_post():
    db=Db()
    eleid=request.form['eleid']
    elname=request.form['elname']
    datetime=request.form['datetime']
    status=request.form['status']
    qry=db.update("update election set elename='"+elname+"',dateandtime='"+datetime+"',status='"+status+"' where eleid='"+eleid+"'")
    return adm_view_election()

@app.route('/adm_delete_election/<id>')
def adm_delete_election(id):
    db=Db()
    qry=db.delete("delete from election where eleid='"+id+"'")
    return adm_view_election()








@app.route('/adm_add_post')
def adm_add_post():
    return render_template("admin/post_add.html")

@app.route('/adm_add_post_post',methods=['post'])
def adm_add_post_post():
    pnm=request.form['postname']
    qry="INSERT INTO post(postname)values ('"+pnm+"')"
    db=Db()
    db.insert(qry)
    return "<script>alert('Post Added');window.location='/adm_add_post';</script>"

@app.route('/adm_view_post')
def adm_view_post():
    db=Db()
    qry=db.select('select * from post')
    return render_template("admin/post_view.html",data=qry)

@app.route('/adm_edit_post/<id>')
def adm_edit_post(id):
    db=Db()
    qry=db.selectOne("select *from post where postid='"+id+"'")
    return render_template("admin/post_edit.html",data=qry)

@app.route('/adm_update_post_post',methods=["post"])
def adm_update_post_post():
    db=Db()
    pstnm=request.form['idd']
    postname=request.form['postname']
    qry=db.update("update post set postname='"+postname+"' where postid='"+pstnm+"'")
    return adm_view_post()

@app.route('/adm_delete_post/<id>')
def adm_delete_post(id):
    db=Db()
    qry=db.delete("delete from post where postid='"+id+"'")
    return adm_view_post()










@app.route('/adm_add_candidate')
def adm_add_candidate():
    db=Db()
    # qry="select * from student"
    qry="select * from student where stuid not in (select candidateid from candidate)"
    res=db.select(qry)
    qry2="select * from post"
    pes=db.select(qry2)
    return render_template("admin/candidate_add.html",data=res,data2=pes)

@app.route('/adm_add_candidate_post',methods=['post'])
def adm_add_candidate_post():
    db=Db()
    cname=request.form["select"]
    nominee=request.form["select1"]
    support=request.form["select2"]
    post=request.form["pst"]
    qry=db.insert("insert into candidate(candidateid,support1,support2,postid)values('"+cname+"','"+nominee+"','"+support+"','"+post+"')")
    return "<script>alert('information added');window.location='/adm_add_candidate';</script>"

@app.route('/adm_view_candidate')
def adm_view_candidate():
    db=Db()
    #select candidate.cid,student.stuname,post.postname,student.stuname as sname, student.stuname as s2name from student,candidate,post where student.stuid=candidate.candidateid and candidate.postid=post.postid and student.stuid=candidate.support1 and student.stuid=candidate.support2
    qr="select candidate.cid,student.stuname,s1.stuname as supporter1,s2.stuname as supporter2,post.postname from candidate inner join post on post.postid=candidate.postid inner join student on candidate.candidateid=student.stuid inner join student as s1 on candidate.support1=s1.stuid inner join student as s2 on candidate.support2=s2.stuid"
    qry3=db.select(qr)

    return render_template("admin/candidate_view.html",data=qry3)

@app.route('/adm_edit_candidate/<id>')
def adm_edit_candidate(id):
    db=Db()
    qry1=db.selectOne("select * from candidate where cid='"+id+"'")

    cand_ifo=db.selectOne("select * from student where stuid='"+str(qry1["candidateid"])+"'")

    sup_one=db.selectOne("select * from student where stuid='"+str(qry1["support1"])+"'")
    sup_two=db.selectOne("select * from student where stuid='"+str(qry1["support2"])+"'")
    postt=db.selectOne("select * from post where postid='"+str(qry1["postid"])+"'")
    qry2=db.select("select * from student")
    qry4=db.select("select * from post")
    session['cdid']=id
    # print(session['cdid'])
    return render_template("admin/candidate_edit.html",candinfo=cand_ifo,supprtone=sup_one,supprttwo=sup_two,post=postt,st=qry2,st1=qry2,st2=qry2,pst=qry4)


@app.route('/adm_update_candidate_post',methods=["post"])
def adm_update_candidate_post():
    db=Db()
    x=session['cdid']
    candidateid=request.form['select']
    support1=request.form['select1']
    support2=request.form['select2']
    postid=request.form['select3']
    qry=db.update("update candidate set candidateid='"+candidateid+"',support1='"+support1+"',support2='"+support2+"',postid='"+postid+"' where cid='"+str(x)+"'")

    return adm_view_candidate()


@app.route('/adm_delete_candidate/<id>')
def adm_delete_candidate(id):
    db=Db()
    qry=db.delete("delete from candidate where cid='"+id+"'")
    return adm_view_candidate()


@app.route('/face_recognition',methods=['post'])
def face_recognition():

    try:
        import face_recognition

        qry = "SELECT `student`.* FROM `student` order by stuid limit 4"
        db = Db()
        res = db.select(qry)
        # print(res)


        known_faces = []
        stud_id = []
        k=0
        for i in res:

            # print(i['image'])
            img = "C:/backend"+i['image']
            # print(img)
            b_img = face_recognition.load_image_file(img)
            b_imgs = face_recognition.face_encodings(b_img)[0]
            known_faces.append(b_imgs)
            stud_id.append(i['stuid'])
            k=k+1
            if k> 5:
                break
            print(stud_id)
        # print("1")

        photo=request.form["photo"]
        # print(photo)

        import base64

        with open("C:\\backend\\static\\imageToSave.jpg", "wb") as fh:
            fh.write(base64.b64decode(photo))


        # known_image = face_recognition.load_image_file("C:\\backend\\static\\faiz5.jpg")
        unknown_image = face_recognition.load_image_file("c:\\backend\\static\\imageToSave.jpg")
        # print(unknown_image)

        indux = 0
        unknown_faces = []

        detecteduserids = []
        indxc = 0

        m = len(face_recognition.face_encodings(unknown_image))
        # print(m);

        ids=""

        print("printing results")
        for a in range(m):
            s = face_recognition.face_encodings(unknown_image)[a]
            unknown_encoding = face_recognition.face_encodings(unknown_image)[a]
            results = face_recognition.compare_faces(known_faces, unknown_encoding,tolerance=0.45)

            for i in range(0,len(results)):
                if results[i]==True:
                    print("stud id " +str(stud_id[i]))
                    return jsonify(status="ok",id=stud_id[i])
        return "", 400
    except Exception as e:
        print(str(e))





@app.route('/adm_add_electionvote')
def adm_add_electionvote():
    db=Db()
    qry="select * from student"
    mes=db.select(qry)
    qry1="select student.stuname,candidate.candidateid from student,candidate where student.stuid=candidate.candidateid"
    ves=db.select(qry1)
    return render_template("admin/electionvote_add.html",data=mes,data1=ves)

@app.route('/adm_add_electionvote_post',methods=['post'])
def adm_view_electionvote_post():
    db=Db()
    stuname=request.form['select']
    cname=request.form['select1']
    dateandtime=request.form['dateandtime']
    qry=db.insert("insert into elevote(stuid,candid,dateandtime) values('"+stuname+"','"+cname+"','"+dateandtime+"')")
    return '''<script>alert('information added');window.location.href='/adm_add_electionvote';</script>'''

@app.route('/adm_view_electionvote')
def adm_view_electionvote():
    db=Db()
    qry=db.select("select * from post");
    # qry=db.select("select student.stuname,post.postname,candidate.stuname as candidatename,elevote.* from student,post inner join elevote on  student.stuid=elevote.stuid inner join student as candidate on  candidate.stuid=elevote.candid  ")
    return render_template("admin/electionvote_view.html",data=qry)

@app.route('/adm_view_result_post',methods=['post'])
def adm_view_result_post():
    db=Db()
    post=request.form['select']
    qry=db.select("select candidate.candidateid,post.postid,course.coursename,student.stuname,student.phoneno,student.email,student.image,count(candidate.candidateid) as 'c' from candidate,student,post,course,elevote where candidate.candidateid=student.stuid and course.courseid=student.courseid and post.postid=candidate.postid and elevote.candid=candidate.candidateid and post.postid='"+post+"' group by(candidateid)")
    print(qry)
    return render_template("admin/electionvote_view.html",data1=qry)







@app.route('/adm_edit_electionvote/<id>')
def adm_edit_electionvote(id):
    db=Db()
    session["evid"]=id
    qry=db.selectOne("select * from elevote where evid='"+id+"' ")
    db = Db()
    stun=db.selectOne("select * from student where stuid='"+str(qry["stuid"])+"' ")
    db = Db()
    # print(stun)
    cnm=db.selectOne("select * from candidate where candidateid='"+str(qry["candid"])+"'")
    db = Db()
    qry1=db.select("select * from student")
    db = Db()
    qry2=db.select("select student.stuname,candidate.candidateid from student,candidate where student.stuid=candidate.candidateid")
    return render_template("admin/electionvote_edit.html",stunm=stun,cnam=cnm,ct=qry1,ao=qry2,data=qry)

@app.route('/adm_update_elevote_post',methods=["post"])
def adm_update_elevote_post():
    db=Db()
    stname=request.form['select']
    pname=request.form['candi']
    dateandtime=request.form['dateandtime']
    qr="update elevote set stuid='"+stname+"',candid='"+pname+"',dateandtime='"+dateandtime+"' where evid='"+str( session["evid"])+"'"
    # print(qr)
    qry=db.update(qr)
    return adm_view_electionvote()

@app.route('/adm_delete_electionvote/<id>')
def adm_delete_electionvote(id):
    db=Db()
    qry=db.delete("delete from elevote where evid='"+id+"'")
    return adm_view_electionvote()










@app.route('/adm_add_winner')
def adm_add_winner():
    db=Db()
    qry=db.select("select * from student")
    qry1=db.select("select * from post")
    return render_template("admin/winner_add.html",data=qry,data1=qry1)


@app.route('/adm_add_winner_post',methods=['post'])
def adm_add_winner_post():
    db=Db()
    stuname=request.form['select']
    postname=request.form['select1']
    yearfrom=request.form['yearfrom']
    yearto=request.form['yearto']
    qry=db.insert("insert into winner(studentname,postname,yearfrom,yearto) values('"+stuname+"','"+postname+"','"+yearfrom+"','"+yearto+"')")
    return "<script>alert('information added');window.location='/adm_add_winner';</script>"

@app.route('/adm_view_winner')
def adm_view_winner():
    db=Db()
    qry=db.select("select * from winner")
    return render_template("admin/winner_view.html",data=qry)

@app.route('/adm_edit_winner/<id>')
def adm_edit_winner(id):
    db=Db()
    qry=db.selectOne("select * from winner where winnerid='"+id+"'")
    stu_n=db.selectOne("select * from student where stuid='"+str(qry["stuid"])+"'")
    postt=db.selectOne("select * from post where postid='"+str(qry["postid"])+"'")
    qry1=db.select("select * from student")
    qry2=db.select("select * from post")
    session['cid']=id
    return render_template("admin/winner_edit.html",stuname=stu_n,post=postt,stt=qry1,stt2=qry2,data=qry)

@app.route('/adm_update_winner_post',methods=["post"])
def adm_update_winner_post():
    db=Db()
    x=session['cid']
    stunm=request.form["select"]
    postnm=request.form["select1"]
    yearfrom=request.form["yearfrom"]
    yearto=request.form["yearto"]
    qry=db.update("update winner set stuid='"+stunm+"',postid='"+postnm+"',yearfrom='"+yearfrom+"',yearto='"+yearto+"' where winnerid='"+str(x)+"'")
    return adm_view_winner()



@app.route('/adm_delete_winner/<id>')
def adm_delete_winner(id):
    db=Db()
    qry=db.delete("delete from winner where winnerid='"+id+"'")
    return adm_view_winner()


# .............................android.........................................................................................


@app.route('/')
def adm_login():
    return render_template("index.html")
@app.route('/adm_login_post',methods=['post'])
def adm_login_post():
    db=Db()
    usnm=request.form['uname']
    pssv=request.form['pass']
    qry=db.selectOne("select * from login where username='"+usnm+"' and password='"+pssv+"'")
    if qry is not None:
        if qry["type"]=="admin":
            return render_template('blank.html')
        else:
            return "<script>alert('incorrect password');window.location='/';</script>"
    else:
        return "<script>alert('incorrect password');window.location='/';</script>"

@app.route('/adm_view_login')
def adm_view_login():
    return render_template("admin/login_view.html")

@app.route('/view_profile',methods=['post'])
def view_profile():
    db=Db()
    uid=request.form['idd']
    print("uid "+ uid )
    qry=db.selectOne("select course.coursename,student.* from student,course where course.courseid=student.courseid and stuid='"+uid+"'")

    print(qry)
    return jsonify(status='ok',name=qry['stuname'],admno=qry['admno'],course=qry['coursename'],semester=qry['semester'],gender=qry['gender'],guardian=qry['guardian'],dob=qry['dob'],phone=qry['phoneno'],email=qry['email'],image=qry['image'])


@app.route('/login_profile')
def login_profile():
    return jsonify()

@app.route('/view_winner',methods=['post'])
def view_winner():
    db=Db()
    qry=db.select("select * from winner")
    # print(qry)
    return jsonify(status="ok",data=qry)

@app.route('/view_candidate',methods=['post'])
def view_candidate():
    db=Db()
    uid=request.form['uid']
    rr="select distinct(post.postid),post.postname from candidate,student,post where student.stuid=candidate.candidateid and post.postid=candidate.postid and post.postid not in (select distinct(candidate.postid) from candidate,elevote where candidate.candidateid=elevote.candid and elevote.stuid='"+uid+"')"
    qry=db.select(rr)
    # print(qry)
    if len(qry)>0:
        return jsonify(status="ok",data=qry)
    else:
        return jsonify(status="no")


@app.route('/view_canddate',methods=['post'])
def view_canddate():
    db=Db()
    postid=request.form['postid']
    qry=db.select("select student.stuname,student.stuid from candidate,post,student where candidate.candidateid=student.stuid and candidate.postid=post.postid and post.postid='"+postid+"'")
    # print(qry)
    return jsonify(status="ok",data=qry)

@app.route('/View_notification',methods=['post'])
def View_notification():
    db=Db()

    qry=db.select("select * from notification")
    return jsonify(status="ok",data=qry)





@app.route('/cast_vote',methods=['post'])
def cast_vote():
    db=Db()
    stuname=request.form['stuid']
    candname=request.form['candid']
    qry=db.insert("insert into elevote(stuid,candid,dateandtime) values('"+stuname+"','"+candname+"',curdate())")
    return jsonify(status="ok",data=qry)



@app.route('/adm_logout')
def adm_logout():
    return render_template("admin/login.html")


@app.route("/a")
def a():
    return render_template("blank.html")



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
