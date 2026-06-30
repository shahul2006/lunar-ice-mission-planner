import { Card, CardContent, Typography, Box } from "@mui/material";

export default function ImageCard({
  title,
  image = null,
}) {
  return (
    <Card
      sx={{
        width: 520,
        background: "#10213b",
        color: "white",
        borderRadius: 3,
        boxShadow: 5,
      }}
    >
      <CardContent>
        <Typography
          variant="h6"
          sx={{
            mb: 2,
            textAlign: "center",
            fontWeight: "bold",
            color: "#90caf9",
          }}
        >
          {title}
        </Typography>

        <Box
          sx={{
            height: 420,
            borderRadius: 2,
            border: "2px dashed #355b87",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            overflow: "hidden",
            background: "#07111f",
          }}
        >
          {image ? (
            <img
              src={image}
              alt={title}
              style={{
                width: "100%",
                height: "100%",
                objectFit: "contain",   // <-- changed from cover
              }}
            />
          ) : (
            <Typography
              sx={{
                color: "#78909c",
              }}
            >
              No Image Available
            </Typography>
          )}
        </Box>
      </CardContent>
    </Card>
  );
}