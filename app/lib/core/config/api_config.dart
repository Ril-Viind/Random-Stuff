/// API configuration for the Pathly app.
///
/// Points to the production backend by default. For local development,
/// override at build/run time:
///   flutter run --dart-define=PATHLY_API_BASE_URL=http://10.0.2.2:8000
abstract final class ApiConfig {
  static const String baseUrl = String.fromEnvironment(
    'PATHLY_API_BASE_URL',
    defaultValue: 'https://pathly-backend-stra.onrender.com',
  );
}
