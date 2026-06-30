import { AppBar, Toolbar, Typography, Box } from "@mui/material";

export default function Navbar() {
  return (
    <AppBar
      position="static"
      sx={{
        background: "#081229",
        boxShadow: 4,
      }}
    >
      <Toolbar>
        <Typography
          variant="h5"
          sx={{
            fontWeight: "bold",
            letterSpacing: 1,
          }}
        >
          🌕 Chandrayaan-2 Mission Planner
        </Typography>

        <Box sx={{ flexGrow: 1 }} />

        <Typography
          variant="body1"
          sx={{
            color: "#d1d5db",
          }}
        >
          ISRO Hackathon 2026
        </Typography>
      </Toolbar>
    </AppBar>
  );
}