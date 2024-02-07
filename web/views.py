from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.db import connections
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_type='Student'
        with connections['user_database'].cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_user WHERE email=%s AND password=%s AND user_type=%s", [email, password, user_type])
            user_data = cursor.fetchone()
        if user_data:
            return redirect('teams',user_data[0])
        else:
            messages.error(request, "Username or Password is incorrect!")
            return render(request, "website/index.html", {'error': 'Invalid login credentials'})
    return render(request, "website/index.html")


def teams(request,pk):
    student_id=pk
    with connections['user_database'].cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_team_member WHERE student_id=%s", [student_id])
            user_data = cursor.fetchall()
    team_ids=[]
    all_teams=[]
    teams={}
    if user_data:
        for i in user_data:
            team_ids.append(i[1])
        for i in team_ids:
            with connections['user_database'].cursor() as cursor:
                cursor.execute("SELECT * FROM tbl_team WHERE id=%s", [i])
                team_data = cursor.fetchone()
                all_teams.append(team_data)
        for i in all_teams:
            teams[i[0]]=i[1]
    context={'pk':pk, 'user':user_data, 'teams':teams}
    return render(request, 'website/teams.html', context)

def course_outline(request, pk, sk):
    student_id=pk
    team_id=sk
    with connections['user_database'].cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_team_member WHERE student_id=%s", [student_id])
            user_data = cursor.fetchone()
            print(user_data)
    with connections['user_database'].cursor() as cursor:
            cursor.execute("SELECT * FROM tbl_team WHERE id=%s", [team_id])
            team_data = cursor.fetchone()
    context = {"pk": pk, "sk": sk, 'user':user_data, 'team':team_data}
    return render(request, "website/outline.html", context)


def record_of_invention(request, pk, sk):
    record = (
        recordOfInvention.objects.filter(teamId=sk).order_by("-date_updated").first()
    )
    if request.method == "POST":
        name = request.POST.get("name_of_invention")
        problem = request.POST.get("problem_it_solves")
        if record == None:
            recordOfInvention.objects.create(
                userId=pk,
                teamId=sk,
                name_of_invention=name,
                problem_it_solves=problem,
            )
            return redirect("statement_of_originality", pk, sk)
        if name != record.name_of_invention or problem != record.problem_it_solves:
            recordOfInvention.objects.create(
                userId=pk,
                teamId=sk,
                name_of_invention=name,
                problem_it_solves=problem,
            )
            return redirect("statement_of_originality", pk, sk)
        return redirect("statement_of_originality", pk, sk)
    context = {"pk": pk, "sk": sk, "record": record}
    return render(request, "website/record_of_invention.html", context)


def statement_of_originality(request, pk, sk):
    statement = (
        statementOfOriginality.objects.filter(teamId=sk)
        .order_by("-date_updated")
        .first()
    )
    if request.method == "POST":
        inventor1 = request.POST.get("inventor1")
        schoolnamegrade1 = request.POST.get("schoolnamegrade1")
        sig1 = request.POST.get("sig1")
        date1 = request.POST.get("date1")

        inventor2 = request.POST.get("inventor2")
        schoolnamegrade2 = request.POST.get("schoolnamegrade2")
        sig2 = request.POST.get("sig2")
        date2 = request.POST.get("date2")

        inventor3 = request.POST.get("inventor3")
        schoolnamegrade3 = request.POST.get("schoolnamegrade3")
        sig3 = request.POST.get("sig3")
        date3 = request.POST.get("date3")

        inventor4 = request.POST.get("inventor4")
        schoolnamegrade4 = request.POST.get("schoolnamegrade4")
        sig4 = request.POST.get("sig4")
        date4 = request.POST.get("date4")

        inventor5 = request.POST.get("inventor5")
        schoolnamegrade5 = request.POST.get("schoolnamegrade5")
        sig5 = request.POST.get("sig5")
        date5 = request.POST.get("date5")
        
        inventor1=Inventor.objects.create(
            inventor=inventor1,
            schoolnamegrade=schoolnamegrade1,
            sig=sig1,
            date=date1
        )
        inventor2=Inventor.objects.create(
            inventor=inventor2,
            schoolnamegrade=schoolnamegrade2,
            sig=sig2,
            date=date2
        )
        inventor3=Inventor.objects.create(
            inventor=inventor3,
            schoolnamegrade=schoolnamegrade3,
            sig=sig3,
            date=date3
        )
        inventor4=Inventor.objects.create(
            inventor=inventor4,
            schoolnamegrade=schoolnamegrade4,
            sig=sig4,
            date=date4
        )
        inventor5=Inventor.objects.create(
            inventor=inventor5,
            schoolnamegrade=schoolnamegrade5,
            sig=sig5,
            date=date5
        )

        statement_of_originality_instance = statementOfOriginality.objects.create(
            userId=pk,
            teamId=sk,
        )
        statement_of_originality_instance.inventors.add(inventor1, inventor2, inventor3, inventor4, inventor5)

        return redirect("flowchart", pk, sk)
    if (statement): context = {"pk": pk, "sk": sk, "statement": statement,"inventors": statement.inventors.all}
    else: context = {"pk": pk, "sk": sk, "statement": statement}
    return render(request, "website/statement_of_originality.html", context)


def flowchart(request, pk, sk):
    if request.method == "POST":
        return redirect("step_1", pk, sk)
    context = {"pk": pk, "sk": sk}
    return render(request, "website/flowchart.html", context)


def step_1(request, pk, sk):
    step1 = stepOne.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        identify_problems = request.POST.get("initial_problem")
        if step1 == None:
            stepOne.objects.create(
                userId=pk,
                teamId=sk,
                identify_problems=identify_problems,
            )
            return redirect("step_2", pk, sk)
        if identify_problems != step1.identify_problems:
            stepOne.objects.create(
                userId=pk,
                teamId=sk,
                identify_problems=identify_problems,
            )
            return redirect("step_2", pk, sk)
        return redirect("step_2", pk, sk)
    context = {"pk": pk, "sk": sk, "step1": step1}
    return render(request, "website/step_1.html", context)


def step_2(request, pk, sk):
    step2 = stepTwo.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        problem_1 = request.POST.get("problem_1")
        problem_2 = request.POST.get("problem_2")
        problem_3 = request.POST.get("problem_3")
        problem_4 = request.POST.get("problem_4")

        p1name1 = request.POST.get("p1name1")
        p1name2 = request.POST.get("p1name2")
        p1name3 = request.POST.get("p1name3")
        p1name4 = request.POST.get("p1name4")
        p1age1 = request.POST.get("p1age1")
        p1age2 = request.POST.get("p1age2")
        p1age3 = request.POST.get("p1age3")
        p1age4 = request.POST.get("p1age4")
        p1comment1 = request.POST.get("p1comment1")
        p1comment2 = request.POST.get("p1comment2")
        p1comment3 = request.POST.get("p1comment3")
        p1comment4 = request.POST.get("p1comment4")

        p2name1 = request.POST.get("p2name1")
        p2name2 = request.POST.get("p2name2")
        p2name3 = request.POST.get("p2name3")
        p2name4 = request.POST.get("p2name4")
        p2age1 = request.POST.get("p2age1")
        p2age2 = request.POST.get("p2age2")
        p2age3 = request.POST.get("p2age3")
        p2age4 = request.POST.get("p2age4")
        p2comment1 = request.POST.get("p2comment1")
        p2comment2 = request.POST.get("p2comment2")
        p2comment3 = request.POST.get("p2comment3")
        p2comment4 = request.POST.get("p2comment4")

        p3name1 = request.POST.get("p3name1")
        p3name2 = request.POST.get("p3name2")
        p3name3 = request.POST.get("p3name3")
        p3name4 = request.POST.get("p3name4")
        p3age1 = request.POST.get("p3age1")
        p3age2 = request.POST.get("p3age2")
        p3age3 = request.POST.get("p3age3")
        p3age4 = request.POST.get("p3age4")
        p3comment1 = request.POST.get("p3comment1")
        p3comment2 = request.POST.get("p3comment2")
        p3comment3 = request.POST.get("p3comment3")
        p3comment4 = request.POST.get("p3comment4")

        p4name1 = request.POST.get("p4name1")
        p4name2 = request.POST.get("p4name2")
        p4name3 = request.POST.get("p4name3")
        p4name4 = request.POST.get("p4name4")
        p4age1 = request.POST.get("p4age1")
        p4age2 = request.POST.get("p4age2")
        p4age3 = request.POST.get("p4age3")
        p4age4 = request.POST.get("p4age4")
        p4comment1 = request.POST.get("p4comment1")
        p4comment2 = request.POST.get("p4comment2")
        p4comment3 = request.POST.get("p4comment3")
        p4comment4 = request.POST.get("p4comment4")

        problem_title = request.POST.get("problem_title")
        problem_description = request.POST.get("problem_description")

        describe_problem = request.POST.get("describe_problem")
        specific_solution = request.POST.get("specific_solution")

        member1 = Problem.objects.create(
            problem=problem_1,
            name1=p1name1,
            name2=p1name2,
            name3=p1name3,
            name4=p1name4,
            age1=p1age1,
            age2=p1age2,
            age3=p1age3,
            age4=p1age4,
            comment1=p1comment1,
            comment2=p1comment2,
            comment3=p1comment3,
            comment4=p1comment4,
        )
        member2 = Problem.objects.create(
            problem=problem_2,
            name1=p2name1,
            name2=p2name2,
            name3=p2name3,
            name4=p2name4,
            age1=p2age1,
            age2=p2age2,
            age3=p2age3,
            age4=p2age4,
            comment1=p2comment1,
            comment2=p2comment2,
            comment3=p2comment3,
            comment4=p2comment4,
        )
        member3 = Problem.objects.create(
            problem=problem_3,
            name1=p3name1,
            name2=p3name2,
            name3=p3name3,
            name4=p3name4,
            age1=p3age1,
            age2=p3age2,
            age3=p3age3,
            age4=p3age4,
            comment1=p3comment1,
            comment2=p3comment2,
            comment3=p3comment3,
            comment4=p3comment4,
        )
        member4 = Problem.objects.create(
            problem=problem_4,
            name1=p4name1,
            name2=p4name2,
            name3=p4name3,
            name4=p4name4,
            age1=p4age1,
            age2=p4age2,
            age3=p4age3,
            age4=p4age4,
            comment1=p4comment1,
            comment2=p4comment2,
            comment3=p4comment3,
            comment4=p4comment4,
        )

        step_two_instance = stepTwo.objects.create(
            userId=pk,
            teamId=sk,
            problem_title=problem_title,
            problem_description=problem_description,
            describe_problem=describe_problem,
            specific_solution=specific_solution,
        )
        step_two_instance.problems.add(member1, member2, member3, member4)

        return redirect("step_3", pk, sk)
    if (step2): context = {"pk": pk, "sk": sk, "step2": step2, "members": step2.problems.all}
    else: context = {"pk": pk, "sk": sk, "step2": step2}
    return render(request, "website/step_2.html", context)


def step_3(request, pk, sk):
    step3 = stepThree.objects.filter(teamId=sk).order_by("-date_updated").first()
    step2 = stepTwo.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        factors = request.POST.get("factors")
        ways_to_solve = request.POST.get("ways_to_solve")
        research = request.POST.get("research")
        difference = request.POST.get("difference")
        if step3 == None:
            stepThree.objects.create(
                userId=pk,
                teamId=sk,
                factors=factors,
                ways_to_solve=ways_to_solve,
                research=research,
                difference=difference,
            )
            return redirect("step_4", pk, sk)
        elif (
            factors != step3.factors
            or ways_to_solve != step3.ways_to_solve
            or research != step3.research
            or difference != step3.difference
        ):
            stepThree.objects.create(
                userId=pk,
                teamId=sk,
                factors=factors,
                ways_to_solve=ways_to_solve,
                research=research,
                difference=difference,
            )
            return redirect("step_4", pk, sk)
        return redirect("step_4", pk, sk)
    context = {"pk": pk, "sk": sk, "step3": step3, "step2": step2}
    return render(request, "website/step_3.html", context)


def step_4(request, pk, sk):
    step4 = stepFour.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        blueprint = request.FILES.get("blueprint")
        teacher_name = request.POST.get("teacher_name")
        teacher_sign = request.POST.get("teacher_sign")
        date = request.POST.get("date")
        i1expert = request.POST.get("i1expert")
        i1credentials = request.POST.get("i1credentials")
        i1identified = request.POST.get("i1identified")
        i1problemface = request.POST.get("i1problemface")
        i2expert = request.POST.get("i2expert")
        i2credentials = request.POST.get("i2credentials")
        i2identified = request.POST.get("i2identified")
        i2problemface = request.POST.get("i2problemface")
        i3expert = request.POST.get("i3expert")
        i3credentials = request.POST.get("i3credentials")
        i3identified = request.POST.get("i3identified")
        i3problemface = request.POST.get("i3problemface")
        sol_design_problem = request.POST.get("sol_design_problem")
        green_sol = request.POST.get("green_sol")
        issue1=Issue.objects.create(
            expert=i1expert, credentials=i1credentials, identified=i1identified, problemface=i1problemface
        )
        issue2=Issue.objects.create(
            expert=i2expert, credentials=i2credentials, identified=i2identified, problemface=i2problemface
        )
        issue3=Issue.objects.create(
            expert=i3expert, credentials=i3credentials, identified=i3identified, problemface=i3problemface
        )
        step_four_instance = stepFour.objects.create(
                userId=pk,
                teamId=sk,
                teacher_name=teacher_name,
                teacher_sign=teacher_sign,
                date=date,
                sol_design_problem=sol_design_problem,
                green_sol=green_sol,
            )
        step_four_instance.issues.add(issue1,issue2,issue3)
        if blueprint == None:
            step_four_instance.blueprint=step4.blueprint
        else:
            step_four_instance.blueprint=blueprint
        print(blueprint)
        return redirect("step_5", pk, sk)
    if (step4): context = {"pk": pk, "sk": sk, "step4": step4,'issues':step4.issues.all}
    else: context = {"pk": pk, "sk": sk, "step4": step4}
    return render(request, "website/step_4.html", context)


def step_5(request, pk, sk):
    step5 = stepFive.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        materials = request.POST.get("materials")
        findings = request.POST.get("findings")
        credit = request.POST.get("credit")
        if step5 == None:
            stepFive.objects.create(
                userId=pk,
                teamId=sk,
                materials=materials,
                findings=findings,
                credit=credit,
            )
            return redirect("step_6", pk, sk)
        elif (
            materials != step5.materials
            or findings != step5.findings
            or credit != step5.credit
        ):
            stepFive.objects.create(
                userId=pk,
                teamId=sk,
                materials=materials,
                findings=findings,
                credit=credit,
            )
            return redirect("step_6", pk, sk)
        return redirect("step_6", pk, sk)
    context = {"pk": pk, "sk": sk, "step5": step5}
    return render(request, "website/step_5.html", context)


def step_6(request, pk, sk):
    step6 = stepSix.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        notes = request.POST.get("notes")
        prototype_pic = request.FILES.get("prototype_pic")
        if step6 == None:
            stepSix.objects.create(
                userId=pk,
                teamId=sk,
                notes=notes,
                prototype_pic=prototype_pic,
            )
            return redirect("step_7", pk, sk)
        if prototype_pic == None:
            stepSix.objects.create(
                userId=pk,
                teamId=sk,
                notes=notes,
                prototype_pic=step6.prototype_pic,
            )
            return redirect("step_7", pk, sk)
        elif notes != step6.notes or prototype_pic != step6.prototype_pic:
            stepSix.objects.create(
                userId=pk,
                teamId=sk,
                notes=notes,
                prototype_pic=prototype_pic,
            )
            return redirect("step_7", pk, sk)
        return redirect("step_7", pk, sk)
    context = {"pk": pk, "sk": sk, "step6": step6}
    return render(request, "website/step_6.html", context)


def step_7(request, pk, sk):
    step7 = stepSeven.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        testing = request.POST.get("testing")
        positive = request.POST.get("positive")
        negative = request.POST.get("negative")
        if step7 == None:
            stepSeven.objects.create(
                userId=pk,
                teamId=sk,
                testing=testing,
                positive=positive,
                negative=negative,
            )
            return redirect("step_8", pk, sk)
        elif (
            testing != step7.testing
            or positive != step7.positive
            or negative != step7.negative
        ):
            stepSeven.objects.create(
                userId=pk,
                teamId=sk,
                testing=testing,
                positive=positive,
                negative=negative,
            )
            return redirect("step_8", pk, sk)
        return redirect("step_8", pk, sk)
    context = {"pk": pk, "sk": sk, "step7": step7}
    return render(request, "website/step_7.html", context)


def step_8(request, pk, sk):
    step8 = stepEight.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        nameinvention = request.POST.get("nameinvention")
        benefits = request.POST.get("benefits")
        price = request.POST.get("price")
        buy = request.POST.get("buy")
        customer_age = request.POST.get("customer_age")
        customer_gender = request.POST.get("customer_gender")
        customer_education = request.POST.get("customer_education")
        customer_house = request.POST.get("customer_house")
        customer_marital = request.POST.get("customer_marital")
        other_notes = request.POST.get("other_notes")
        stepEight.objects.create(
            userId=pk,
            teamId=sk,
            nameinvention=nameinvention,
            benefits=benefits,
            price=price,
            buy=buy,
            customer_age=customer_age,
            customer_gender=customer_gender,
            customer_education=customer_education,
            customer_house=customer_house,
            customer_marital=customer_marital,
            other_notes=other_notes,
        )
        return redirect("survey", pk, sk)
    context = {"pk": pk, "sk": sk, "step8": step8}
    return render(request, "website/step_8.html", context)


def survey(request, pk, sk):
    survey = surveyLogbook.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        things_enjoyed = request.POST.get("things_enjoyed")
        thanking = request.POST.get("thanking")
        difficulty = request.POST.get("difficulty")
        future = request.POST.get("future")
        if survey == None:
            surveyLogbook.objects.create(
                userId=pk,
                teamId=sk,
                things_enjoyed=things_enjoyed,
                thanking=thanking,
                difficulty=difficulty,
                future=future,
            )
            return redirect("logbook_complete", pk, sk)
        elif (
            things_enjoyed != survey.things_enjoyed
            or thanking != survey.thanking
            or difficulty != survey.difficulty
            or future != survey.future
        ):
            surveyLogbook.objects.create(
                userId=pk,
                teamId=sk,
                things_enjoyed=things_enjoyed,
                thanking=thanking,
                difficulty=difficulty,
                future=future,
            )
            return redirect("logbook_complete", pk, sk)
        return redirect("logbook_complete", pk, sk)
    context = {"pk": pk, "sk": sk, "survey": survey}
    return render(request, "website/survey.html", context)


def logbook_complete(request, pk, sk):
    context = {"pk": pk, "sk": sk, "survey": survey}
    return render(request, "website/logbook_complete.html", context)


def notes(request, pk, sk):
    note = Note.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        note_title = request.POST.get("note_title")
        note_desc = request.POST.get("note_desc")
        if note == None:
            Note.objects.create(
                userId=pk,
                teamId=sk,
                note_title=note_title,
                note_desc=note_desc,
            )
            return redirect("preview_logbook", pk, sk)
        elif note_title != note.note_title or note_desc != note.note_desc:
            Note.objects.create(
                userId=pk,
                teamId=sk,
                note_title=note_title,
                note_desc=note_desc,
            )
            return redirect("preview_logbook", pk, sk)
        return redirect("preview_logbook", pk, sk)
    context = {"pk": pk, "sk": sk, "note": note}
    return render(request, "website/notes.html", context)


def preview_logbook(request, pk, sk):
    record = (
        recordOfInvention.objects.filter(teamId=sk).order_by("-date_updated").first()
    )
    statement = (
        statementOfOriginality.objects.filter(teamId=sk)
        .order_by("-date_updated")
        .first()
    )
    step1 = stepOne.objects.filter(teamId=sk).order_by("-date_updated").first()
    step2 = stepTwo.objects.filter(teamId=sk).order_by("-date_updated").first()
    step3 = stepThree.objects.filter(teamId=sk).order_by("-date_updated").first()
    step4 = stepFour.objects.filter(teamId=sk).order_by("-date_updated").first()
    step5 = stepFive.objects.filter(teamId=sk).order_by("-date_updated").first()
    step6 = stepSix.objects.filter(teamId=sk).order_by("-date_updated").first()
    step7 = stepSeven.objects.filter(teamId=sk).order_by("-date_updated").first()
    step8 = stepEight.objects.filter(teamId=sk).order_by("-date_updated").first()
    survey = surveyLogbook.objects.filter(teamId=sk).order_by("-date_updated").first()
    note = Note.objects.filter(teamId=sk).order_by("-date_updated").first()
    context = {
        "pk": pk,
        "sk": sk,
        "record": record,
        "statement": statement,
        "step1": step1,
        "step2": step2,
        "step3": step3,
        "step4": step4,
        "step5": step5,
        "step6": step6,
        "step7": step7,
        "step8": step8,
        "survey": survey,
        "note": note,
    }
    return render(request, "website/preview_logbook.html", context)
