<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title> dash board</title>
    <!-- Custom fonts for this template-->
    {% load static %}
		<link  rel="stylesheet" href="{% static 'fontawesome/css/all.min.css' %}">
		<link href="{% static 'css/sb-admin-2.min.css' %}" rel="stylesheet">
		<link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
		<link href="{% static 'css/style.css' %}" rel="stylesheet">
		<link href="{% static 'css/style3.css' %}" rel="stylesheet">
		<link rel="stylesheet" href="{% static 'css/style3.css' %}">
</head>

<body id="page-top">


<!-- Page Wrapper -->
  <div id="wrapper">
    <!-- Sidebar -->
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

      <!-- Sidebar - Brand -->
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.php">
			<div>
		<img src="{% static 'img/log.svg' %}" class="img-fluid">
        </div>
      </a>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">

      <!-- Nav Item - Dashboard -->
      <li class="nav-item active">
        <a class="nav-link" href="index.php" class="text-center">
          <i class="fas fa-user user-font px-4"></i></a></li>

        <!-- Divider -->
	   <li class="nav-item">
        <a class="nav-link collapsed" href="{% url 'student-leavephp' %}" >
          <i class="fas fa-user-graduate"></i>
          <span>Student leave</span>
        </a>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="{% url 'assessment_php' %}" >
          <i class="fas fa-chalkboard-teacher"></i>
          <span>Assessments</span>
        </a>

      </li>

      <!-- Attendance Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="{% url 'attendence_1_php' %}" >
          <i class="fas fa-school"></i>
          <span>Attendance</span>
        </a>
      </li>
      <li class="nav-item">
        <a class="nav-link collapsed" href="#">
          <i class="fas fa-bell"></i>
          <span>Notifications</span>
        </a>
      </li>

      <!-- Nav Item -ptrevious details-->
      <li class="nav-item">
        <a class="nav-link" href="">
          <i class="fas fa-info-circle"></i>
          <span>Previous details</span></a>
      </li>
	  <li class="nav-item">
        <a class="nav-link" href="">
          <i class="fas fa-info-circle"></i>
          <span>Course Materials</span></a>
      </li>
      <!-- Sidebar Toggler (Sidebar) -->
      <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
      </div>

    </ul>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">

        <!-- Topbar -->
		<div class="container-fliud">
        <nav class="navbar navbar-expand navbar-light topbar mb-4 static-top shadow bg-gradient-primary">
		<!-- Sidebar Toggle (Topbar) -->
          <button id="sidebarToggleTop" class="btn btn-link d-md-none rounded-circle  bg-light">
            <i class="fa fa-bars"></i>
          </button>
		 <!-- Topbar Navbar -->
          <ul class="navbar-nav ml-auto pr-5 p-hide">

            <!-- Nav Item - Alerts -->
            <li class="nav-item ">
              <a class="nav-link " href=#>
                <i class="fas fa-home"><p> Home</p></i>
              </a>
              
            </li>
			<li class="nav-item">
              <a class="nav-link " href="{% url 'facprofile' %}"  >
                <i class="fas fa-user "><p> Myprofile</p></i>
              </a>
              
            </li>
			<li class="nav-item">
              <a class="nav-link " href="#">
                <i class="fas fa-info"> <p>Help</p></i>
              </a>
              
            </li>
			<li class="nav-item">
              <a class="nav-link " href="#"  >
                <i class="fas fa-bell "><p> Notification</p></i>
              </a>
              
            </li>
			<li class="nav-item">
              <a class="nav-link " href="{% url 'logouts' %}" >
                <i class="fas fa-sign-out-alt  text-gray"><p>LogOut</p></i>
              </a>
            </li>

          </ul>

        </nav>
		
		
					
	
			
			
			
					
<!------------------------------content start------------------------------->
<!------------------------------------------section start----------------------------------------------->
<form action="{% url 'marksubmit'%}" method="POST">
				{% csrf_token %}
				<table class="table table-striped">
						<tr><td>student_name: </td><td><input type="text" placeholder="" class="frm" name="student_name"></td></tr>
                        <tr><td>assess_no: </td><td><input type="text" placeholder="" class="frm" name="assess_no"></td></tr>
                        <tr><td>max_mark: </td><td><input type="text" placeholder="" class="frm" name="max_mark"></td></tr>

                        <tr><td>subject_1: </td><td><input type="text" placeholder="" class="frm" name="subject_1"></td></tr>
                        <tr><td>subject_2: </td><td><input type="text" class="frm" name="subject_2"></td></tr>
						<tr><td>subject_3: </td><td><input type="text" class="frm" placeholder="" name="subject_3"></td>
						<tr><td>subject_4: </td><td><input type="text" placeholder="" class="frm" name="subject_4"></td></tr>
                        <tr><td>subject_5: </td><td><input type="text" class="frm" placeholder="" name="subject_5"></td></tr>
				</table>
						<br><input type="submit" class="but1" value="Register"></input>
						<input type="submit" class="but2" value="Cancel"></input>
				
				</form>
<!------------------------------------------section end------------------------------------------------->
<!------------------------------content end------------------------------->
 <!-- Footer -->
      <footer class="">
          <div class="copyright text-center bg-gradient-primary py-2 text-light">
            <span>Copyright &copy; Orisys Academy 2019-2020</span>
        </div>
      </footer>
      <!-- End of Footer -->
</div>
    </div>
    <!-- End of Content Wrapper -->


  <!-- Bootstrap core JavaScript-->
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="css/proper.min.js"></script>
  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin-2.js"></script>
</body>

</html>
