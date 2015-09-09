#include "ElectroMagn.h"
#include "Profile.h"

using namespace std;

struct ExtFieldStructure;

// Default constructor.
// Applies to profiles for species (density, velocity and temperature profiles)
Profile::Profile(ProfileStructure & pp, unsigned int nvar) :
profile_param(pp){
    init(nvar);
}


// Special constructor.
// Applies to external field profiles
Profile::Profile(ExtFieldStructure & pp, unsigned int nvar):
profile_param(static_cast<ProfileStructure> (pp))
{
    init(nvar);
}

// Preliminary functions
// that evaluate a python function with various numbers of arguments
double Evaluate1var(PyObject * fun, std::vector<double> x_cell) {
    return PyTools::runPyFunction(fun, x_cell[0]);
}
double Evaluate2var(PyObject * fun, std::vector<double> x_cell) {
    return PyTools::runPyFunction(fun, x_cell[0], x_cell[1]);
}
double Evaluate3var(PyObject * fun, std::vector<double> x_cell) {
    return PyTools::runPyFunction(fun, x_cell[0], x_cell[1], x_cell[2]);
}


void Profile::init(unsigned int nvariables)
{
    if      ( nvariables == 1 ) Evaluate = &Evaluate1var;
    else if ( nvariables == 2 ) Evaluate = &Evaluate2var;
    else if ( nvariables == 3 ) Evaluate = &Evaluate3var;
    else {
        ERROR("A profile has been defined with unsupported number of variables");
    }
}

double Profile::valueAt(vector<double> x_cell) {
    
    return (*Evaluate)(profile_param.py_profile, x_cell);
    
}
