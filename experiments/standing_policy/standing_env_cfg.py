"""Standing-only configuration for Unitree G1."""

from mjlab.tasks.velocity.config.g1.env_cfgs import (  # ty:ignore[unresolved-import]
  unitree_g1_flat_env_cfg,  # ty:ignore[unresolved-import]
)


def unitree_g1_standing_env_cfg(play: bool = False):
  cfg = unitree_g1_flat_env_cfg(play=play)

  # Modify command to only generate zero velocity (standing)
  cfg.commands["twist"].ranges.lin_vel_x = (0.0, 0.0)
  cfg.commands["twist"].ranges.lin_vel_y = (0.0, 0.0)
  cfg.commands["twist"].ranges.ang_vel_z = (0.0, 0.0)
  cfg.commands["twist"].rel_standing_envs = 1.0  # Always standing

  return cfg
