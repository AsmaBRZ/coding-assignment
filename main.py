from database import Database
import json

print("Example 1")
# Initial graph
build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract = {"img001": ["A"], "img002": ["C1"]}
# Graph edits
edits = [("A1", "A"), ("A2", "A")]
if len(build) > 0:
    # Build graph
    print("Initial graph")
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    print("Edited graph")
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()



print("\n\nExample 2")
# Initial graph
build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract = {"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
# Graph edits
edits = [("A1", "A"), ("A2", "A"), ("C2", "C")]
#self.status={0:'valid', 1:'granularity_staged', 2:'coverage_staged', 3:'invalid'}
# Get status (this is only an example, test your code as you please as long as it works)
status = {}
if len(build) > 0:
    # Build graph
    print("Initial graph")
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    print("Edited graph")
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()


print("\n\nExample 3")#read data and convert it to python dictionary
expected_status = json.loads(open("data/expected_status.json", "r").read())
graph_build = json.loads(open("data/graph_build.json", "r").read())
graph_edits = json.loads(open("data/graph_edits.json", "r").read())
img_extract = json.loads(open("data/img_extract.json", "r").read())

# Initial graph
build = graph_build
# Extract
extract = img_extract
# Graph edits
edits = graph_edits
#self.status={0:'valid', 1:'granularity_staged', 2:'coverage_staged', 3:'invalid'}
# Get status (this is only an example, test your code as you please as long as it works)
status = {}
if len(build) > 0:
    # Build graph
    print("Initial graph")
    db = Database(build[0][0])
    if len(build) > 1:
    	db.add_nodes(build[1:])
    # Add extract
    print("Edited graph")
    db.add_extract(extract)
    # Graph edits
    db.add_nodes(edits)
    # Update status
    status = db.get_extract_status()
#Status VS expected_status comparaison
print("\n\nAre the computed results teh same as the expected one ?" ,status == expected_status)
