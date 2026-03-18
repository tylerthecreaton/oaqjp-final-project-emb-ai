"""Run unit tests and display detailed results."""

import sys
import unittest

# Load and run tests from 5a_unit_testing
loader = unittest.TestLoader()
suite = loader.loadTestsFromName("5a_unit_testing")

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Print summary
print("\n" + "=" * 70)
print("TEST SUMMARY")
print("=" * 70)
print(f"Tests run: {result.testsRun}")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")
print(f"Success: {result.wasSuccessful()}")

if result.wasSuccessful():
    print("\n✓ ALL TESTS PASSED")
else:
    print("\n✗ SOME TESTS FAILED")
    sys.exit(1)
