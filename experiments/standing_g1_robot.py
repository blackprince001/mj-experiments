"""Standing-only configuration for Unitree G1."""

from mjlab.tasks.registry import register_mjlab_task
from mjlab.tasks.velocity.config.g1.env_cfgs import unitree_g1_flat_env_cfg
from mjlab.tasks.velocity.config.g1.rl_cfg import unitree_g1_ppo_runner_cfg
from mjlab.tasks.velocity.rl import VelocityOnPolicyRunner


def unitree_g1_standing_env_cfg(play: bool = False):
  cfg = unitree_g1_flat_env_cfg(play=play)

  # Modify command to only generate zero velocity (standing)
  cfg.commands["twist"].ranges.lin_vel_x = (0.0, 0.0)
  cfg.commands["twist"].ranges.lin_vel_y = (0.0, 0.0)
  cfg.commands["twist"].ranges.ang_vel_z = (0.0, 0.0)
  cfg.commands["twist"].rel_standing_envs = 1.0  # Always standing

  return cfg


# Register the standing task
register_mjlab_task(
  task_id="Mjlab-Standing-Flat-Unitree-G1",
  env_cfg=unitree_g1_standing_env_cfg(),
  play_env_cfg=unitree_g1_standing_env_cfg(play=True),
  rl_cfg=unitree_g1_ppo_runner_cfg(),
  runner_cls=VelocityOnPolicyRunner,
)
    