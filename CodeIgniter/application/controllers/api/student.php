<?php
require (APPPATH.'/libraries/REST_Controller.php');
require (APPPATH.'libraries/Format.php');

// use namespace
use Restserver\Libraries\REST_Controller;

class Student extends REST_Controller{
    public function __construct(){
        parent::__construct();
        //load database
        $this->load->database();
        $this->load->model(array("api/student_model"));
        $this->load->library("form_validation");
    }

    /*
        INSERT: POST REQUEST TYPE
        UPDATE: PUT REQUEST TYPE
        DELETE: DELETE REQUEST TYPE
        LIST: GET REQUEST TYPE
    */

    // POST: <project url>/index.php/api/student
    public function index_post(){ 
        //insert data method
        //print_r($this->input->post());die;

        //collecting form data input
        $name = $this->input->post("name");
        $email = $this->input->post("email");
        $mobile = $this->input->post("mobile");
        $course = $this->input->post("course");

        //form validation for inputs
        $this->form_validation->set_rules("name", "Name", "required");
        $this->form_validation->set_rules("email", "Email", "required|valid_email");
        $this->form_validation->set_rules("mobile", "Mobile", "required");
        $this->form_validation->set_rules("course", "Course", "required");

        // checking form submission have any error or not
        if($this->form_validation->run() === FALSE){
            // we have some errors
            $this->response(array(
                "status" => 0,
                "message" => "All field are needed"
            ), REST_Controller::HTTP_NOT_FOUND);
        }
        else{
            if(!empty($name) && !empty($email) && !empty($mobile) && !empty($course)){
                // all values are available
                $student = array(
                    "name"=>$name,
                    "email"=>$email,
                    "mobile"=>$mobile,
                    "course"=>$course
                );
                
                $result = $this->student_model->insert_student($student);
    
                if($result){
                    $this->response(array(
                        "status" => 1,
                        "message" => "Student has been created"
                    ), REST_Controller::HTTP_OK);
                }
                else{
                    $this->response(array(
                        "status" => 0,
                        "message" => "Failed to create student"
                    ), REST_Controller::HTTP_INTERNAL_SERVER_ERROR);
                }
            }
            else{
                // we have some empty fields
                $this->response(array(
                    "status" => 0,
                    "message" => "All fields are needed"
                ), REST_Controller::HTTP_NOT_FOUND);
            }
        }

        /*
        $data = json_decode(file_get_contents("php://input"));

        $name = isset($data->name)? $data->name: "";
        $email = isset($data->email)? $data->email: "";
        $mobile = isset($data->mobile)? $data->mobile: "";
        $course = isset($data->course)? $data->course: "";
        */

    }

    // PUT: <project url>/index.php/api/student
    public function index_put(){
        //update data method
        //echo "This is PUT Method";
        $data = json_decode(file_get_contents("php://input"));
        
        if(isset($data->id) && isset($data->name) && isset($data->email) && isset($data->mobile) && isset($data->course)){
            $student_id = $data->id;
            $student_info = array(
                "name" => $data->name,
                "email" => $data->email,
                "mobile" => $data->mobile,
                "course" => $data->course
            );

            $result = $this->student_model->update_student_information($student_id, $student_info);

            if($result){
                $this->response(array(
                    "status" => 1,
                    "message" => "Student data updated successfully"
                ), REST_Controller::HTTP_OK);
            }
            else{
                $this->response(array(
                    "status" => 0,
                    "message" => "Failed to update student data"
                ), REST_Controller::HTTP_INTERNAL_SERVER_ERROR);
            }
        }
        else{
            $this->response(array(
                "status" => 0,
                "message" => "All fields are needed"
            ), REST_Controller::HTTP_NOT_FOUND);
        }
        
   }

   // DELETE: <project url>/index.php/api/student
   public function index_delete(){
        //delete data method
        $data = json_decode(file_get_contents("php://input"));
        $student_id = $data->student_id;

        $result = $this->student_model->delete_student($student_id);

        if($result){
            //return true
            $this->response(array(
                "status" => 1,
                "message" => "Student has been deleted"
            ), REST_Controller::HTTP_OK);
        }
        else{
            //return false
            $this->response(array(
                "status" => 0,
                "message" => "Failed to delete student"
            ), REST_Controller::HTTP_NOT_FOUND);
        }
        
   }

   // GET: <project url>/index.php/api/student
   public function index_get(){
        //list data method
        //echo "This is GET Method";
       
        $students = $this->student_model->get_students();

        //print_r($result);
        /*
        $this->response(array(
            "status" => 1,
            "message" => "Students found",
            "data"=> $query->result()
        ), 200);
        */

        if(count($students)>0){
            $this->response(array(
                "status" => 1,
                "message" => "Students found",
                "data"=> $students
            ), REST_Controller::HTTP_OK);
        }
        else{
            $this->response(array(
                "status" => 0,
                "message" => "No Students found",
                "data"=> $students
            ), REST_Controller::HTTP_NOT_FOUND);
        }
   }
}

?>