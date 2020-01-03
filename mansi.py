m = open("Mansi.html","w")
a = """<html>
 <head>
<title>RESUME</title>

<style type="text/css">
    table {
        font-size: 20px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body>
<div >
  <center><h1><u>MY RESUME</u></h1></center>  
<h3> Mansi Soni</h3>
<p>Adress : Indira Gandhi Girls Hostel Bhopal</p>
<p>DOB: 4-10-2000</p>
<p>Narayan Nagar Bhopal</p
<p>Contact No.:  6265 613 868</p>
 
  <h2><u>CAREER OBJECTIVE</u></h2>
  <p>To succeed in an environment of growth 
     and excellence in computer science and 
     earn a job which provide me job satisfaction
     and self development and help me in achieving
      personal as well as organization goals.</p>
            <h2><u>EDUCATION </u></h2>
            <table border="1">
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Excellence School Balaghat</td>
                    <td> 78%</td>
                    <td>2016</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td>Excellence School Balaghat</td>
                    <td>65%</td>
                    <td>2018</td>
                </tr>
                <tr>
                    <td>1st Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>5.60 SGPA</td>
                    <td>2019</td>
                </tr>
                <tr>
                    <td>2nd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>6.16 SGPA</td>
                    <td>2019</td>
                </tr>
                
            </table>
        </div>
         <h2><u>HOBBIES</u></h2>
          <p> Listening</p>
           <p>Music</p>
           <p>Art </p>
           <p>Craft</p>
           <p></p>

          <h2><u>LANGUAGES</u></h2>
           <p>Hindi</p>
           <p>English.</p> 
          <h2><u>SKILLS</u></h2>
           <p>C,C++ and HTML.</p>
         <h2><u>WORK  EXPERIENCE</u></h2>
        <p>Fresher.</p>

</body>
</html>"""
m.write(a)
m.close()