import { Box, CircularProgress, Typography } from "@mui/material";

export default function LoadingSpinner({
  message = "Analyzing Chandrayaan-2 Dataset..."
}) {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        py: 6,
      }}
    >
      <CircularProgress
        size={70}
        thickness={5}
        sx={{
          color: "#64b5f6",
        }}
      />

      <Typography
        variant="h6"
        sx={{
          mt: 3,
          color: "#ffffff",
          fontWeight: "bold",
        }}
      >
        {message}
      </Typography>

      <Typography
        variant="body2"
        sx={{
          mt: 1,
          color: "#90caf9",
        }}
      >
        Please wait while the mission data is being processed...
      </Typography>
    </Box>
  );
}