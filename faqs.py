"""
CodeAlpha FAQ Chatbot Dataset
=============================
Realistic university/college FAQ pairs covering admissions, fees, courses,
exams, results, hostel, library, scholarships, transport, campus life,
clubs, internships, and placements.
Author: Jenicadeva Christa S
"""

FAQ_DATA = [
    # ── Admissions ──────────────────────────────────────────────────────────
    {"question": "How do I apply for admission?",
     "answer": "You can apply online through our official admissions portal by filling out the application form, uploading your documents, and paying the application fee."},
    {"question": "What documents are required for admission?",
     "answer": "You need your 10th and 12th mark sheets, transfer certificate, migration certificate, passport-size photos, and a valid ID proof."},
    {"question": "What is the last date to apply for admission?",
     "answer": "Admissions typically close by the end of July, but exact dates are published on the college website each academic year."},
    {"question": "Is there an entrance exam for admission?",
     "answer": "Yes, most programs require qualifying scores in entrance exams such as JEE, NEET, or our own college entrance test, depending on the course."},
    {"question": "Can I apply for multiple courses at once?",
     "answer": "Yes, you can apply for up to three courses in a single application, and you will be considered for each based on eligibility."},
    {"question": "What is the eligibility criteria for undergraduate admission?",
     "answer": "You must have completed 12th grade with a minimum of 50% aggregate marks from a recognized board, with subject requirements varying by course."},
    {"question": "Do you offer lateral entry admission?",
     "answer": "Yes, diploma holders can apply for lateral entry directly into the second year of relevant engineering programs."},
    {"question": "How can I check my admission status?",
     "answer": "You can log into the admissions portal using your application ID and password to track your application status in real time."},

    # ── Fees ────────────────────────────────────────────────────────────────
    {"question": "What is the total tuition fee for the course?",
     "answer": "Tuition fees vary by program and range from ₹60,000 to ₹1,50,000 per year. Please check the fee structure page for your specific course."},
    {"question": "What are the hostel fees?",
     "answer": "Hostel fees range from ₹45,000 to ₹70,000 per year depending on room type (shared or single) and included meal plans."},
    {"question": "Can I pay the fees in installments?",
     "answer": "Yes, the college allows fee payment in two or three installments per semester. Contact the accounts office to set up a payment plan."},
    {"question": "What payment methods are accepted for fees?",
     "answer": "We accept online payments via debit card, credit card, net banking, and UPI, as well as demand drafts at the accounts office."},
    {"question": "Is there a late fee penalty?",
     "answer": "Yes, a late fee of ₹500 per week is charged if fees are not paid by the due date mentioned in the fee schedule."},
    {"question": "Are there any refundable deposits?",
     "answer": "Yes, the caution deposit of ₹5,000 is refundable at the end of your course, provided there are no pending dues or damages."},

    # ── Courses ─────────────────────────────────────────────────────────────
    {"question": "What courses does the college offer?",
     "answer": "We offer undergraduate and postgraduate programs in Engineering, Computer Science, Business Administration, Commerce, and Arts & Sciences."},
    {"question": "What is the duration of the engineering course?",
     "answer": "The undergraduate engineering program is a 4-year course divided into 8 semesters."},
    {"question": "Can I switch my branch after first year?",
     "answer": "Branch change requests are considered after the first year based on your CGPA and seat availability in the desired branch."},
    {"question": "Are there any online or part-time courses available?",
     "answer": "Yes, we offer select part-time postgraduate diploma and certificate courses, including some fully online programs."},
    {"question": "What is the medium of instruction?",
     "answer": "All courses are taught in English, with some humanities electives optionally available in regional languages."},
    {"question": "Is there an option to pursue a minor degree?",
     "answer": "Yes, students can opt for a minor specialization alongside their major from the third semester onward, subject to credit requirements."},

    # ── Exams ───────────────────────────────────────────────────────────────
    {"question": "When are the semester exams conducted?",
     "answer": "Semester exams are usually held in the last two weeks of May and November each year, as per the official academic calendar."},
    {"question": "What is the minimum attendance required to sit for exams?",
     "answer": "Students must maintain a minimum of 75% attendance in each subject to be eligible to appear for semester exams."},
    {"question": "How can I apply for a re-exam or supplementary exam?",
     "answer": "You can apply for supplementary exams through the student portal within two weeks of result declaration, along with the prescribed fee."},
    {"question": "What happens if I miss an exam due to illness?",
     "answer": "Submit a medical certificate to the examination office within 3 days, and you may be granted a special exam opportunity."},
    {"question": "Are exams conducted online or offline?",
     "answer": "All major semester exams are conducted offline on campus, while some internal assessments may be held online."},
    {"question": "How many backlogs are allowed to continue to the next semester?",
     "answer": "Students can carry forward a maximum of 4 backlog subjects while progressing to the next semester, as per academic regulations."},

    # ── Results ─────────────────────────────────────────────────────────────
    {"question": "When will the semester results be announced?",
     "answer": "Results are typically declared within 3 to 4 weeks after the completion of semester exams and published on the student portal."},
    {"question": "How can I check my exam results?",
     "answer": "Log into the student portal with your roll number and password, then navigate to the Results section to view your scorecard."},
    {"question": "Can I apply for revaluation of my answer sheet?",
     "answer": "Yes, revaluation requests can be submitted online within 7 days of result declaration along with the revaluation fee per subject."},
    {"question": "How is the CGPA calculated?",
     "answer": "CGPA is calculated as the credit-weighted average of grade points earned across all semesters completed so far."},

    # ── Hostel ──────────────────────────────────────────────────────────────
    {"question": "Is hostel accommodation available for all students?",
     "answer": "Hostel accommodation is available for both boys and girls on a first-come, first-served basis, subject to seat availability."},
    {"question": "What facilities are provided in the hostel?",
     "answer": "Hostels are equipped with Wi-Fi, laundry service, a common room, study halls, mess facilities, and 24/7 security."},
    {"question": "Can I choose my roommate in the hostel?",
     "answer": "Yes, you can submit a roommate preference request during hostel registration, though it depends on room availability."},
    {"question": "What is the hostel curfew time?",
     "answer": "The hostel gates close at 9:30 PM on weekdays and 10:30 PM on weekends, with prior permission required for late entry."},
    {"question": "Is mess food included in the hostel fee?",
     "answer": "Yes, the hostel fee includes a mandatory mess plan covering breakfast, lunch, and dinner on all weekdays and weekends."},

    # ── Library ─────────────────────────────────────────────────────────────
    {"question": "What are the library timings?",
     "answer": "The central library is open from 8:00 AM to 8:00 PM on weekdays and 9:00 AM to 5:00 PM on weekends."},
    {"question": "How many books can I borrow from the library?",
     "answer": "Undergraduate students can borrow up to 3 books at a time for a period of 14 days, renewable once if not reserved by others."},
    {"question": "Does the library provide access to digital journals?",
     "answer": "Yes, the library subscribes to several digital journal databases like IEEE, Springer, and JSTOR, accessible with your student login."},
    {"question": "What happens if I lose a library book?",
     "answer": "You will need to pay the replacement cost of the book along with a processing fine as determined by the library department."},

    # ── Scholarships ────────────────────────────────────────────────────────
    {"question": "What scholarships are available for students?",
     "answer": "We offer merit-based scholarships, need-based financial aid, and government scholarships for SC/ST/OBC and minority students."},
    {"question": "How do I apply for a scholarship?",
     "answer": "Scholarship applications can be submitted through the student portal along with income certificates and academic records during the designated window."},
    {"question": "Is there a scholarship for sports achievements?",
     "answer": "Yes, students who represent the college at state or national level sports events are eligible for sports scholarships covering partial tuition fees."},

    # ── Transport ───────────────────────────────────────────────────────────
    {"question": "Does the college provide bus transportation?",
     "answer": "Yes, the college operates bus routes covering major areas of the city, with fees charged separately per semester based on the route."},
    {"question": "How can I register for the college bus service?",
     "answer": "You can register for bus transport through the transport office during admission or at the start of each semester."},
    {"question": "What are the bus timings?",
     "answer": "College buses typically depart from designated stops between 7:00 AM and 8:00 AM and return after college hours around 4:30 PM."},

    # ── Campus ──────────────────────────────────────────────────────────────
    {"question": "What facilities are available on campus?",
     "answer": "The campus features modern labs, a central library, sports complex, cafeteria, medical center, auditorium, and high-speed Wi-Fi throughout."},
    {"question": "Is Wi-Fi available across the campus?",
     "answer": "Yes, high-speed Wi-Fi is available in all academic buildings, hostels, and common areas across the campus."},
    {"question": "Does the college have a gym or sports facilities?",
     "answer": "Yes, we have a fully equipped gym, basketball and volleyball courts, a cricket ground, and an indoor games room for students."},
    {"question": "Is there a medical center on campus?",
     "answer": "Yes, the campus has a medical center staffed with a nurse and visiting doctor available on weekdays for basic healthcare needs."},

    # ── Clubs ───────────────────────────────────────────────────────────────
    {"question": "What clubs and societies can I join?",
     "answer": "We have technical clubs, a coding club, robotics society, drama club, music club, and various cultural and literary societies."},
    {"question": "How do I join a college club?",
     "answer": "You can join any club by registering during the orientation week or by contacting the club coordinator directly through the student portal."},
    {"question": "Are there any technical fests organized by the college?",
     "answer": "Yes, the college organizes an annual technical fest featuring hackathons, coding competitions, robotics challenges, and workshops."},

    # ── Internships ─────────────────────────────────────────────────────────
    {"question": "Does the college help students find internships?",
     "answer": "Yes, the Training and Placement Cell actively connects students with internship opportunities through industry partnerships and job portals."},
    {"question": "Is internship mandatory for graduation?",
     "answer": "Yes, students must complete a minimum 6-week internship in their pre-final or final year as part of the graduation requirements."},
    {"question": "How do I get credit for my internship?",
     "answer": "Submit your internship completion certificate and a report to your department coordinator to receive internship credit toward your degree."},

    # ── Placements ──────────────────────────────────────────────────────────
    {"question": "What is the average placement package offered?",
     "answer": "The average placement package is around ₹6 LPA, with the highest packages going up to ₹24 LPA in recent placement drives."},
    {"question": "Which companies visit the campus for placements?",
     "answer": "Companies like TCS, Infosys, Wipro, Amazon, and several other IT and core engineering firms regularly visit for campus placements."},
    {"question": "When do placement drives usually start?",
     "answer": "Placement drives typically begin in the seventh semester, around August and September, and continue through the final semester."},
    {"question": "Is placement assistance provided for all branches?",
     "answer": "Yes, the Training and Placement Cell supports students from all branches with resume building, mock interviews, and aptitude training."},
]
