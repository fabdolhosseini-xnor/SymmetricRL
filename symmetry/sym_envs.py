from .env_utils import register_symmetric_env

# Symmetric_Walker2DBulletEnv-v0
register_symmetric_env(
    "pybullet_envs:Walker2DBulletEnv-v0",
    {
        #### observation:
        "com_obs_inds": [0, 2, 3, 5, 7],
        "neg_obs_inds": [1, 4, 6],
        "left_obs_inds": list(range(8, 14)) + [20],
        "right_obs_inds": list(range(14, 20)) + [21],
        "sideneg_obs_inds": [],
        #### action:
        "com_act_inds": [],
        "left_act_inds": list(range(0, 3)),
        "right_act_inds": list(range(3, 6)),
        "sideneg_act_inds": [],
    },
)

# Symmetric_HumanoidBulletEnv-v0
register_symmetric_env(
    "pybullet_envs:HumanoidBulletEnv-v0",
    {
        #### observation:
        "com_obs_inds": [
            0,  # z
            2,  # cos(yaw)
            3,  # vx
            5,  # vz
            7,  # pitch
            # common joints
            10,
            11,
        ],
        "neg_obs_inds": [
            1,  # sin(yaw)
            4,  # vy
            6,  # roll
            # neg joints
            8,
            9,
            12,
            13,
        ],
        "left_obs_inds": list(range(22, 30)) + list(range(36, 42)) + [43],
        "right_obs_inds": list(range(14, 22)) + list(range(30, 36)) + [42],
        "sideneg_obs_inds": list(range(30, 34)),
        #### action:
        "com_act_inds": [1],
        "neg_act_inds": [0, 2],
        "left_act_inds": [7, 8, 9, 10, 14, 15, 16],
        "right_act_inds": [3, 4, 5, 6, 11, 12, 13],
        "sideneg_act_inds": [11, 12],
    },
)


# # Symmetric_Walker3DCustomEnv-v0
# register_symmetric_env(
#     "mocca_envs:Walker3DCustomEnv-v0",
#     {
#         #### observation:
#         "com_obs_inds": [0, 1, 3, 5, 7, 51, 28],
#         "left_obs_inds": [
#             14,
#             15,
#             16,
#             17,
#             18,
#             23,
#             24,
#             25,
#             26,
#             35,
#             36,
#             37,
#             38,
#             39,
#             44,
#             45,
#             46,
#             47,
#             49,
#         ],
#         "right_obs_inds": [
#             9,
#             10,
#             11,
#             12,
#             13,
#             19,
#             20,
#             21,
#             22,
#             30,
#             31,
#             32,
#             33,
#             34,
#             40,
#             41,
#             42,
#             43,
#             48,
#         ],
#         "neg_obs_inds": [2, 4, 6, 8, 27, 29, 50],
#         "sideneg_obs_inds": [],
#         #### action:
#         "com_act_inds": [1],
#         "neg_act_inds": [0, 2],
#         "left_act_inds": [8, 9, 10, 11, 12, 17, 18, 19, 20],
#         "right_act_inds": [3, 4, 5, 6, 7, 13, 14, 15, 16],
#         "sideneg_act_inds": [],
#     },
# )

