import {
  Card,
  CardContent,
  Typography,
  Button,
} from "@mui/material";
import UploadFileIcon from "@mui/icons-material/UploadFile";

export default function UploadCard({
  title,
  selectedFile,
  selectedXmlFile,
  onFileSelect,
  onXmlSelect,
}) {
  const handleFileChange = (event) => {
    if (event.target.files.length > 0) {
      onFileSelect(event.target.files[0]);
    }
  };

  const handleXmlChange = (event) => {
    if (event.target.files.length > 0) {
      onXmlSelect(event.target.files[0]);
    }
  };

  const isOHRC = title === "OHRC Dataset";

  return (
    <Card
      sx={{
        width: 300,
        background: "#10213b",
        color: "white",
        borderRadius: 3,
        textAlign: "center",
        p: 2,
        boxShadow: 5,
      }}
    >
      <CardContent>
        <UploadFileIcon
          sx={{
            fontSize: 60,
            color: "#64b5f6",
          }}
        />

        <Typography
          variant="h6"
          sx={{
            mt: 2,
            mb: 2,
            fontWeight: "bold",
          }}
        >
          {title}
        </Typography>

        {/* IMG Upload */}

        <Button
          variant="contained"
          component="label"
          sx={{
            background: "#1976d2",
            mb: 1,
            width: "100%",
          }}
        >
          {isOHRC ? "Upload IMG" : "Upload"}

          <input
            hidden
            type="file"
            onChange={handleFileChange}
          />
        </Button>

        <Typography
          variant="body2"
          sx={{
            color: "#90caf9",
            wordBreak: "break-word",
            mb: isOHRC ? 2 : 0,
          }}
        >
          {selectedFile
            ? selectedFile.name
            : "No file selected"}
        </Typography>

        {/* XML Upload Only for OHRC */}

        {isOHRC && (
          <>
            <Button
              variant="contained"
              component="label"
              sx={{
                background: "#7b1fa2",
                mb: 1,
                width: "100%",
              }}
            >
              Upload XML

              <input
                hidden
                type="file"
                accept=".xml"
                onChange={handleXmlChange}
              />
            </Button>

            <Typography
              variant="body2"
              sx={{
                color: "#ce93d8",
                wordBreak: "break-word",
              }}
            >
              {selectedXmlFile
                ? selectedXmlFile.name
                : "No XML selected"}
            </Typography>
          </>
        )}
      </CardContent>
    </Card>
  );
}