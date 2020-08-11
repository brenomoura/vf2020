import os
import json

import xmltodict
import pandas as pd


def xml_xyz_values_to_tuple(xyz_values):
    new_tuple = tuple(
        map(float, xyz_values.replace("(", "").replace(")", "").split(" "))
    )
    return new_tuple


def body_params_to_df(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())

    out_dict = json.loads(json.dumps(doc))
    vf_dict = {}
    vf_dict.update(
        {
            "wheelbase": float(
                out_dict["afc"]["Subsystem"]["CRTSprungMass"]["@wheelbase"]
            ),
            "cg_longitunidal_front_wheel": float(
                out_dict["afc"]["Subsystem"]["CRTSprungMass"]["@cgX"]
            ),
            "frontDownForceScale": float(
                out_dict["afc"]["Subsystem"]["CRTAerodynamicForces"][
                    "@frontDownForceScale"
                ]
            ),
        }
    )
    return pd.DataFrame(vf_dict, index=[0])


def brakes_params_to_df(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())

    out_dict = json.loads(json.dumps(doc))
    vf_dict = {}
    vf_dict.update(
        {
            "bias_front": float(
                out_dict["afc"]["Subsystem"]["ParameterTree"]["ParameterTree"][0][
                    "FloatParameter"
                ][0]["@value"]
            ),
            "master_cylinder_pressure_gain": float(
                out_dict["afc"]["Subsystem"]["ParameterTree"]["ParameterTree"][0][
                    "FloatParameter"
                ][1]["@value"]
            ),
        }
    )
    return pd.DataFrame(vf_dict, index=[0])


def front_suspension_params_to_df(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())

    out_dict = json.loads(json.dumps(doc))
    vf_dict = {}
    vf_dict.update(
        {
            "front_track_width": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionGeneralProperties"][
                    "@trackWidth"
                ]
            ),
            "front_leftRideHeightSensor": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"][
                    "CRTRideHeightSensor"
                ][0]["@rideHeight"]
            ),
            "front_left_camber": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    0
                ]["@value"]
            ),
            "front_right_camber": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    1
                ]["@value"]
            ),
            "front_left_toe": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    2
                ]["@value"]
            ),
            "front_right_toe": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    3
                ]["@value"]
            ),
        }
    )
    return pd.DataFrame(vf_dict, index=[0])


def rear_suspension_params_to_df(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())

    out_dict = json.loads(json.dumps(doc))
    vf_dict = {}
    vf_dict.update(
        {
            "rear_track_width": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionGeneralProperties"][
                    "@trackWidth"
                ]
            ),
            "rear_leftRideHeightSensor": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"][
                    "CRTRideHeightSensor"
                ][2]["@rideHeight"]
            ),
            "rear_left_camber": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    0
                ]["@value"]
            ),
            "rear_right_camber": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    1
                ]["@value"]
            ),
            "rear_left_toe": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    2
                ]["@value"]
            ),
            "rear_right_toe": float(
                out_dict["afc"]["Subsystem"]["CRTSuspensionSetupData"]["CRTAdjustment"][
                    3
                ]["@value"]
            ),
        }
    )
    return pd.DataFrame(vf_dict, index=[0])


def powertrain_params_to_df(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())

    out_dict = json.loads(json.dumps(doc))
    vf_dict = {}
    vf_dict.update(
        {
            "fl_transmissionRatio": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][4][
                    "@transmissionRatio"
                ]
            ),
            "fl_torqueScalingFactor": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][4][
                    "@torqueScalingFactor"
                ]
            ),
            "fr_transmissionRatio": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][5][
                    "@transmissionRatio"
                ]
            ),
            "fr_torqueScalingFactor": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][5][
                    "@torqueScalingFactor"
                ]
            ),
            "rl_transmissionRatio": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][6][
                    "@transmissionRatio"
                ]
            ),
            "rl_torqueScalingFactor": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][6][
                    "@torqueScalingFactor"
                ]
            ),
            "rr_transmissionRatio": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][7][
                    "@transmissionRatio"
                ]
            ),
            "rr_torqueScalingFactor": float(
                out_dict["afc"]["Subsystem"]["CRTDriveline"]["CRTMotor"][7][
                    "@torqueScalingFactor"
                ]
            ),
        }
    )
    return pd.DataFrame(vf_dict, index=[0])


def get_endurance_results(file_path):
    result_list = []
    with open(file_path, "r") as result:
        for line in result:
            result_list.append(line.replace("\n", ""))
            if "Simulation is complete." in line:
                break

    lap_time_string = result_list[-21]
    lap_time = lap_time_string.replace(">> LAP TIME           = ", "").replace(
        " sec", ""
    )
    return pd.DataFrame({"endurance_laptime": float(lap_time)}, index=[0])


def get_acceleration_results(file_path):
    result_list = []
    with open(file_path, "r") as result:
        for line in result:
            result_list.append(line.replace("\n", ""))
            if "Simulation is complete." in line:
                break

    lap_time_string = result_list[-21]
    lap_time = lap_time_string.replace(">> LAP TIME           = ", "").replace(
        " sec", ""
    )
    return pd.DataFrame({"acceleration_laptime": float(lap_time)}, index=[0])


def get_autox_results(file_path):
    result_list = []
    with open(file_path, "r") as result:
        for line in result:
            result_list.append(line.replace("\n", ""))
            if "Simulation is complete." in line:
                break

    lap_time_string = result_list[-21]
    lap_time = lap_time_string.replace(">> LAP TIME           = ", "").replace(
        " sec", ""
    )
    return pd.DataFrame({"autox_laptime": float(lap_time)}, index=[0])


def get_skidpad_results(file_path):
    result_list = []
    with open(file_path, "r") as result:
        for line in result:
            result_list.append(line.replace("\n", ""))
            if "Simulation is complete." in line:
                break

    lap_time_string = result_list[-21]
    lap_time = lap_time_string.replace(">> LAP TIME           = ", "").replace(
        " sec", ""
    )
    return pd.DataFrame({"skidpad_laptime": float(lap_time)}, index=[0])


def join_dfs(
    body,
    brakes,
    front_suspension,
    rear_suspension,
    powertrain,
    endurance_results,
    acceleration_results,
    autox,
    skidpad,
):
    body_df = body_params_to_df(body)
    brakes_df = brakes_params_to_df(brakes)
    front_suspension_df = front_suspension_params_to_df(front_suspension)
    rear_suspension_df = rear_suspension_params_to_df(rear_suspension)
    powertrain_df = powertrain_params_to_df(powertrain)
    endurance_laptime_df = get_endurance_results(endurance_results)
    acceleration_laptime_df = get_acceleration_results(acceleration_results)
    autox_laptime_df = get_autox_results(autox)
    skidpad_laptime_df = get_skidpad_results(skidpad)
    final_df = pd.concat(
        [
            body_df,
            brakes_df,
            front_suspension_df,
            rear_suspension_df,
            powertrain_df,
            endurance_laptime_df,
            acceleration_laptime_df,
            autox_laptime_df,
            skidpad_laptime_df,
        ],
        axis=1,
    )
    return final_df


body = "VI_Racer_2020.cdb/subsystems.tbl/VI_Racer_body.xml"
brakes = "VI_Racer_2020.cdb/subsystems.tbl/VI_Racer_brakes.xml"
front_suspension = "VI_Racer_2020.cdb/subsystems.tbl/VI_Racer_front_suspension.xml"
rear_suspension = "VI_Racer_2020.cdb/subsystems.tbl/VI_Racer_rear_suspension.xml"
powertrain = "VI_Racer_2020.cdb/subsystems.tbl/VI_Racer_E_powertrain.xml"
endurance_results = "Working_Directory/VI_Racer_E_Endurance_solver_svm.log"
acceleration_results = "Working_Directory/VI_Racer_E_Acceleration_solver_svm.log"
autox_resutls = "Working_Directory/VI_Racer_E_Autocross_solver_svm.log"
skidpad_results = "Working_Directory/VI_Racer_E_Skidpad_solver_svm.log"


final_df = join_dfs(
    body,
    brakes,
    front_suspension,
    rear_suspension,
    powertrain,
    endurance_results,
    acceleration_results,
    autox_resutls,
    skidpad_results,
)


csv_file_name = "RUNSDATA.csv"

if os.path.isfile(csv_file_name):
    final_df.to_csv("RUNSDATA.csv", mode="a", header=False, index=False)
else:
    final_df.to_csv(csv_file_name, index=False)
